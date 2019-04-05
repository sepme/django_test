from django import forms
from accounts.models import Author, Publisher


class AddBook(forms.Form):
    name = forms.CharField(label="Name")
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label="Author Name")
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all(), label="Publisher Name")


class AddAuthor(forms.Form):
    name = forms.CharField(label="Name")


class AddPublisher(forms.Form):
    name = forms.CharField(label="Name")
