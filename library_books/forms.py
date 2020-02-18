from django import forms
from .models import Book

""" add book form """
class AddBook(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'price')


