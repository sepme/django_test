from django.shortcuts import render
import accounts.models as models
from django.views import generic

class BookList(generic.ListView):
    model = models.Book
    template_name = 'profile.html'
