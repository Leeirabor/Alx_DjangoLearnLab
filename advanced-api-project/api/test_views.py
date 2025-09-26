from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book

"""
Test cases for Book API endpoints:
- CRUD operations
- Filtering
- Searching
- Ordering
- Permissions & authentication
Run with: python manage.py test api
"""

class BookAPITests(APITestCase):
    """
    Test suite for the Book API endpoints.
    Covers CRUD, filtering, searching, ordering, and permissions.
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()

        # Create an author
        self.author = Author.objects.create(name="Chinua Achebe")

        # Create a sample book
        self.book = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author
        )

        # Define URLs
        self.list_url = reverse("book-list")  # from your BookListView
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book.id})
        self.all_books_url = "/books_all/"  # from the router

    def test_list_books(self):
        """Test retrieving all books (public endpoint)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_single_book(self):
        """Test retrieving a single book by ID."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Things Fall Apart")

    def test_create_book_requires_authentication(self):
        """Test creating a book requires login."""
        data = {"title": "No Longer at Ease", "publication_year": 1960, "author": self.author.id}
        response = self.client.post(self.all_books_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_book(self):
        """Test logged-in user can create a book."""
        self.client.login(username="testuser", password="password123")
        data = {"title": "Arrow of God", "publication_year": 1964, "author": self.author.id}
        response = self.client.post(self.all_books_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """Test updating a book as authenticated user."""
        self.client.login(username="testuser", password="password123")
        data = {"title": "Things Fall Apart (Updated)", "publication_year": 1958, "author": self.author.id}
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Things Fall Apart (Updated)")

    def test_delete_book(self):
        """Test deleting a book as authenticated user."""
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books_by_title(self):
        """Test filtering books by title."""
        response = self.client.get(f"{self.list_url}?title=Things Fall Apart")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Things Fall Apart")

    def test_search_books(self):
        """Test searching books by author name."""
        response = self.client.get(f"{self.list_url}?search=Achebe")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["author"], self.author.id)

    def test_order_books_by_publication_year(self):
        """Test ordering books by publication year."""
        # Add another book with later year
        Book.objects.create(title="Anthills of the Savannah", publication_year=1987, author=self.author)
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLessEqual(
            response.data[0]["publication_year"], response.data[-1]["publication_year"]
        )
