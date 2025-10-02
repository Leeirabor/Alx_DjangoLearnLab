# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('posts/', views.PostListView.as_view(), name='post-list'),                 # / or /posts/
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'), # /posts/1/
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),    # /posts/new/
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),  # /posts/1/edit/
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'), # /posts/1/delete/
    # keep any auth URLs (login/register/profile) her
]
