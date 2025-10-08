# posts/urls.py
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views import FollowUserView, UnfollowUserView, FollowToggleView

urlpatterns = [
    # existing account routes...
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    # or toggle:
    path('follow-toggle/<int:user_id>/', FollowToggleView.as_view(), name='follow-toggle'),
]
router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"comments", CommentViewSet, basename="comment")

urlpatterns = router.urls
