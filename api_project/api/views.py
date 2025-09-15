from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for CRUD operations on Book model.
    Supports: list, retrieve, create, update, delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
