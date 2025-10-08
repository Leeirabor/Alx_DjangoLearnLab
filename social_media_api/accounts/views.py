# accounts/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser  # or your User model name if different
from .serializers import UserSerializer


class FollowUserView(generics.GenericAPIView):
    """
    Allows an authenticated user to follow another user.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)
        if target_user == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target_user)
        return Response({"detail": f"You are now following {target_user.username}."}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    """
    Allows an authenticated user to unfollow another user.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)
        if target_user == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(target_user)
        return Response({"detail": f"You have unfollowed {target_user.username}."}, status=status.HTTP_200_OK)
