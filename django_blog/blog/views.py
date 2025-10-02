# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm

from .forms import RegisterForm, ProfileForm
from .models import Post
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return redirect('post-detail', pk=post.pk)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10
    ordering = ["-published_date"]


# Public detail view
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


# Authenticated users can create posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    # where to go after successful creation
    success_url = reverse_lazy("post-list")
    login_url = "login"

    def form_valid(self, form):
        # set the logged-in user as author
        form.instance.author = self.request.user
        messages.success(self.request, "Post created successfully.")
        return super().form_valid(form)


# Only the author can update
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post-list")
    login_url = "login"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, "You are not allowed to edit this post.")
        return super().handle_no_permission()


# Only the author can delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")
    login_url = "login"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, "You are not allowed to delete this post.")
        return super().handle_no_permission()

def home(request):
    # simple homepage listing recent posts
    posts = Post.objects.order_by("-published_date")[:10]
    return render(request, "blog/home.html", {"posts": posts})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. Welcome!")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "blog/login.html"
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    template_name = "blog/logout.html"

@login_required
def profile_view(request):
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
