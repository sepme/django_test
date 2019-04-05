from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponseRedirect

import accounts.models as models
from accounts.forms import AddBook, AddAuthor, AddPublisher


class BookList(generic.ListView):
    model = models.Book
    template_name = 'book_list.html'
    context_object_name = 'book_list'


class AuthorList(generic.ListView):
    model = models.Author
    template_name = 'author_list.html'
    context_object_name = 'author_list'


class PublisherList(generic.ListView):
    model = models.Publisher
    template_name = 'publisher_list.html'
    context_object_name = 'publisher_list'


def add_book(request):
    if request.method == 'POST':
        form = AddBook(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            author = form.cleaned_data['author']
            publisher = form.cleaned_data['publisher']
            new_book = models.Book(name=name, author=author, publisher=publisher)
            new_book.save()
            author.book_number += 1
            author.save()
            publisher.book_number += 1
            publisher.save()
            return HttpResponseRedirect(reverse('book_list'))
    else:
        form = AddBook()
    return render(request, 'add_form.html', {'form': form, 'object_name': 'Book'})


def add_author(request):
    if request.method == 'POST':
        form = AddAuthor(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            new_author = models.Author(name=name)
            new_author.save()
            return HttpResponseRedirect(reverse('author_list'))
    else:
        form = AddAuthor()
    return render(request, 'add_form.html', {'form': form, 'object_name': 'Author'})


def add_publisher(request):
    if request.method == 'POST':
        form = AddPublisher(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            new_publisher = models.Publisher(name=name)
            new_publisher.save()
            return HttpResponseRedirect(reverse('publisher_list'))
    else:
        form = AddPublisher()
    return render(request, 'add_form.html', {'form': form, 'object_name': 'Publisher'})
