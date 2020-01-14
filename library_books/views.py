from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

# Create your views here.
def all_books(request):
    books = Book.objects.all().order_by("title")
    return render(request, "books.html", {"books" : books})

def check_out(request):

    checkout = Book.objects.get(id=1)
    if checkout.checkedOut is False:
        checkout.checkedOut = True
    else:
        checkout.checkedOut = False
    checkout.save()
    return render(request, "books.html")