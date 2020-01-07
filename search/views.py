from django.shortcuts import render
from library_books.models import Book
# Create your views here.

def book_search(request):
    books = Book.objects.filter(title__icontains=request.GET['bkSearch'])
    return render(request, "books.html", {"books" : books})
