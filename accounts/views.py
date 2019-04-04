from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect

import accounts.models as models
from accounts.forms import AddBook

class BookList(generic.ListView):
    model = models.Book
    template_name = 'book_list.html'
    context_object_name = 'book_list'

def add_book(request):
    if request.method == 'POST':
        form = AddBook(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            author = form.cleaned_data['author']
            publisher = form.cleaned_data['publisher']
            new_book = models.Book(name=name,author=author,publisher=publisher)
            new_book.save()
            return HttpResponseRedirect('book_list')
    else:
        form = AddBook()
    return render(request, 'add_book.html', {'form':form})
