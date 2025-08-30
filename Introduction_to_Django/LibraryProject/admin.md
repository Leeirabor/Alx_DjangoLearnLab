# Django Admin Integration for Book Model

---

## Registering the Book Model
In `bookshelf/admin.py`, the `Book` model was registered with Django’s admin site:

```python
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)
