# blog/urls.py
from django.urls import path
from . import views
from .views import CommentCreateView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', views.add_comment, name='add-comment'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path("post/<int:pk>/comment/new/", CommentCreateView.as_view(), name="comment-create"),
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path('tags/<str:tag_name>/', views.PostsByTagListView.as_view(), name='posts-by-tag'),
    path('search/', views.SearchResultsView.as_view(), name='search-results'),
    path("tags/<slug:tag_slug>/", views.PostByTagListView.as_view(), name="posts_by_tag"),
]
   # keep any auth URLs (login/register/profile) her
