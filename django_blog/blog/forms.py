# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'}),
        }

class PostForm(forms.ModelForm):
    """
    Form for creating/updating Post instances.
    The author is set in the view (request.user), not by the form.
    """
    class Meta:
        model = Post
        fields = ['title', 'content']  # author & published_date are set automatically
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title'}),
            'content': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Write your post...'}),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email address")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

