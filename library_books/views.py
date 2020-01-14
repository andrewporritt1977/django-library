from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.
def all_books(request):
    books = Book.objects.all().order_by("title")
    return render(request, "books.html", {"books" : books})

def check_out(request, pk):
    books = Book.objects.all().order_by("title")
    book = get_object_or_404(Book, pk=pk) if pk else None
    user = request.user.username
    if book.checkedOut is False:
        book.checkedOut = True
        book.checked_by = user
    else:
        book.checkedOut = False
        book.checked_by = ""
    book.save()
    return render(request, "books.html", {"books" : books})
