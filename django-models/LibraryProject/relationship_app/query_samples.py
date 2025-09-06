from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
books_by_orwell = Book.objects.filter(author__name="George Orwell")

# List all books in a library
library = Library.objects.get(name="library_name")
books_in_library = library.books.all()

# Retrieve the librarian for a library
librarian = library.librarian

# Print results (optional for testing)
print("Books by George Orwell:", [book.title for book in books_by_orwell])
print("Books in Central Library:", [book.title for book in books_in_library])
print("Librarian of Central Library:", librarian.name)
