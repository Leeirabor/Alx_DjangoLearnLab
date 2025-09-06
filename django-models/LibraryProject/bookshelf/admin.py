from django.contrib import admin
from .models import Book
# Register your models here.
# Customize the admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these fields in list view
    list_filter = ('publication_year', 'author')  # Add filters by year and author
    search_fields = ('title', 'author')  # Enable search by title and author

# Register the Book model with the custom admin settings
admin.site.register(Book, BookAdmin)