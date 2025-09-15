from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required


from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookForm


@permission_required("bookshelf.can_create", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # safe: cleaned fields used by ModelForm
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/add_book.html", {"form": form})

# View books (requires can_view)
@permission_required("bookshelf.can_view", raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, "bookshelf/view_books.html", {"books": books})

# Create book (requires can_create)
@permission_required("bookshelf.can_create", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_year = request.POST.get("publication_year")
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return redirect("view_books")
    return render(request, "bookshelf/add_book.html")

# Edit book (requires can_edit)
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_year = request.POST.get("publication_year")
        book.save()
        return redirect("view_books")
    return render(request, "bookshelf/edit_book.html", {"book": book})

# Delete book (requires can_delete)
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("view_books")


# Book list view (requires can_view)
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

# Create book (requires can_create)
@permission_required("bookshelf.can_create", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_year = request.POST.get("publication_year")
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return redirect("book_list")
    return render(request, "bookshelf/add_book.html")

# Edit book (requires can_edit)
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_year = request.POST.get("publication_year")
        book.save()
        return redirect("book_list")
    return render(request, "bookshelf/edit_book.html", {"book": book})

# Delete book (requires can_delete)
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("book_list")
from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False)

def search_books(request):
    form = SearchForm(request.GET)
    books = Book.objects.none()
    if form.is_valid():
        q = form.cleaned_data["q"]
        # use ORM, not raw SQL or string concat
        books = Book.objects.filter(title__icontains=q)
    return render(request, "bookshelf/search.html", {"form": form, "books": books})
