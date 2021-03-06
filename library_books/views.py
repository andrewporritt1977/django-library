from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import AddBook, EditBook

# Main Book View
def all_books(request):
    books = Book.objects.all().order_by("title")
    return render(request, "books.html", {"books" : books})

# Check in / out
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

# archive - intended for 'retired or lost books' 
def archive_book(request, pk):
    books = Book.objects.all().order_by("title")
    book = get_object_or_404(Book, pk=pk) if pk else None
    if book.archived is False:
        book.archived = True
    else:
        book.archived = False
    book.save()
    return render(request, "books.html", {"books" : books})

# CRUD Add
def add_book(request):
    if request.method == "POST":
        form = AddBook(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('books')
    else:
        form = AddBook()
    return render(request, 'add_book.html', {'form' : form})

# CRUD Update
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = EditBook(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('books')
    else:
        form = EditBook(instance=book)
    return render(request, 'edit_book.html', {'form' : form})

# CRUD Delete
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('books')
    return render(request, "delete_book.html", {"object" : book})

        