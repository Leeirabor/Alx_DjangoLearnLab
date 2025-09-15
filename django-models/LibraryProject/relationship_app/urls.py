from django.urls import path
from . import views
from .views import list_books
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # Books and Library Views
    path("books/", views.list_books, name="list_books"),  # function-based view
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),  # class-based view
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Authentication Views
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    


    # Books and Library Views
    
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Authentication Views (using built-in class-based views)
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    # Custom Registration View
    path("register/", views.register_view, name="register"),
    # Role-based views
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
]

