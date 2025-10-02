# blog/urls.py
from django.urls import path
from .views import register_view, profile_view, CustomLoginView, CustomLogoutView

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/", profile_view, name="profile"),
]
