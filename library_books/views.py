from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

# Create your views here.
def all_books(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books" : books})
