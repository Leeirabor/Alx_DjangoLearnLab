# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email address")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ProfileForm(forms.ModelForm):
    """
    Simple profile form for editing a user's basic info.
    Extend this if you add a separate Profile model (profile picture, bio).
    """
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
