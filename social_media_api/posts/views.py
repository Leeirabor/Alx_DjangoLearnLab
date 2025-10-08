from django.shortcuts import render

# Create your views here.
# posts/views.py
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
# posts/views.py
from rest_framework import generics, permissions
from django.conf import settings
from django.db.models import Q
from .models import Post
from django.views.generic import ListView
from .models import Post

class FeedView(ListView):
    model = Post
    template_name = 'posts/feed.html'
    context_object_name = 'posts'

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')



class FeedListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]   # only authenticated users have a feed
    pagination_class = None   # optional: let DRF default pagination apply if you set it in settings

    def get_queryset(self):
        user = self.request.user
        # posts by users this user follows
        # if you want to include the user's own posts in the feed, add user to the queryset:
        # following_qs = user.following.all() | User.objects.filter(pk=user.pk)
        return Post.objects.filter(author__in=user.following.all()).order_by('-created_at')


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    """
    CRUD for posts. List & retrieve are public (per default permission class),
    creating requires authentication, updating/deleting requires author.
    """
    queryset = Post.objects.all().select_related('author').prefetch_related('comments')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["author__username"]          # filter by author
    search_fields = ["title", "content"]            # search by keyword
    ordering_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    CRUD for comments. Comments are linked to posts.
    """
    queryset = Comment.objects.all().select_related("author", "post")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["post", "author__username"]
    search_fields = ["content"]
    ordering_fields = ["created_at", "updated_at"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
