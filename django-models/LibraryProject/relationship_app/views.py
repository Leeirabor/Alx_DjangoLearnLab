from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library
# Create your views here.
# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

# Class-based view: Show details of a specific library
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})