from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import AddBook

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

def add_book(request):
    if request.method =="POST":
        form = AddBook(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('books')
    
    else:
        form = AddBook()
    return render(request, 'add_book.html', {'form' : form})

