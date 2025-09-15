from django import forms
from .models import Book

# Example form to demonstrate CSRF protection and safe input handling
class ExampleForm(forms.Form):
    search_query = forms.CharField(
        max_length=100,
        required=True,
        label="Search",
        widget=forms.TextInput(attrs={"placeholder": "Enter search term"})
    )

# Optional: model form for Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
