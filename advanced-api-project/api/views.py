from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# 1. List all books
class BookListView(generics.ListAPIView):
    """
    API endpoint to retrieve a list of all books.
    Accessible to all users (authenticated or not).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# 2. Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    API endpoint to retrieve a single book by its ID.
    Accessible to all users (authenticated or not).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# 3. Create a new book
class BookCreateView(generics.CreateAPIView):
    """
    API endpoint to create a new book.
    Only authenticated users can create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook to customize save logic if needed.
        Currently saves book directly.
        """
        serializer.save()


# 4. Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    API endpoint to update a book.
    Only authenticated users can update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Hook to allow custom update logic.
        """
        serializer.save()


# 5. Delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    API endpoint to delete a book.
    Only authenticated users can delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
