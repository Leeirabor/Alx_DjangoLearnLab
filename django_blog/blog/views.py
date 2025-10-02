# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

from .forms import RegisterForm, ProfileForm

def register_view(request):
    """
    Handle new user registration.
    Uses RegisterForm (extends UserCreationForm) to collect username/email/password.
    On successful registration the user is logged in and redirected to profile.
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after register
            messages.success(request, "Registration successful. Welcome!")
            return redirect("profile")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "blog/login.html"
    redirect_authenticated_user = True  # already logged-in users are redirected


class CustomLogoutView(LogoutView):
    template_name = "blog/logout.html"


@login_required
def profile_view(request):
    """
    Allow authenticated users to view and edit basic profile info.
    Uses ProfileForm to update first_name, last_name, email.
    """
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})
