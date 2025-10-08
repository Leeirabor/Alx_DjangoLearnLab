# accounts/urls.py
from django.urls import path
from .views import RegisterView, CustomObtainAuthToken, ProfileView, FollowToggleView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomObtainAuthToken.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("follow/<str:username>/", FollowToggleView.as_view(), name="follow-toggle"),
    
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),

]
