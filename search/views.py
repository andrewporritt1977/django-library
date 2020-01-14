from django.shortcuts import render
from library_books.models import Book
# Create your views here.

def book_search(request):
    books = Book.objects.filter(title__icontains=request.GET['bkSearch'])
    return render(request, "books.html", {"books" : books})

def genre_filter(request):
    books = Book.objects.filter(genre__icontains=request.GET['gFilter'])
    return render(request, "books.html", {"books" : books})

def reset_view(request):
    books = books = Book.objects.all().order_by("title")
    return render(request, "books.html", {"books" : books})