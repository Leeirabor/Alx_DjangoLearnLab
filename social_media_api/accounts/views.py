from django.shortcuts import render

# Create your views here.
# accounts/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer
from django.shortcuts import get_object_or_404

User = get_user_model()

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(User, id=user_id)
        if target == request.user:
            return Response({"detail": "Cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        # add target to request.user.following
        request.user.following.add(target)
        return Response({"detail": f"You are now following {target.username}."}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(User, id=user_id)
        if target == request.user:
            return Response({"detail": "Cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(target)
        return Response({"detail": f"You have unfollowed {target.username}."}, status=status.HTTP_200_OK)

# optional: toggle
class FollowToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(User, id=user_id)
        if target == request.user:
            return Response({"detail": "Cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        if target in request.user.following.all():
            request.user.following.remove(target)
            return Response({"detail": f"Unfollowed {target.username}."}, status=status.HTTP_200_OK)
        else:
            request.user.following.add(target)
            return Response({"detail": f"Followed {target.username}."}, status=status.HTTP_200_OK)


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        resp = super().create(request, *args, **kwargs)
        user = User.objects.get(pk=resp.data["id"])
        token, _ = Token.objects.get_or_create(user=user)
        data = resp.data
        data["token"] = token.key
        return Response(data, status=status.HTTP_201_CREATED)

class CustomObtainAuthToken(ObtainAuthToken):
    """
    Returns { token, user_id, username } on successful login.
    """
    def post(self, request, *args, **kwargs):
        resp = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=resp.data["token"])
        user = token.user
        data = {
            "token": token.key,
            "user_id": user.id,
            "username": user.username,
        }
        return Response(data)

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # profile endpoint returns the currently authenticated user profile
        return self.request.user

class FollowToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        try:
            target = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=404)
        user = request.user
        if user == target:
            return Response({"detail": "Cannot follow yourself."}, status=400)
        if user in target.followers.all():
            target.followers.remove(user)  # unfollow
            return Response({"detail": "Unfollowed."})
        else:
            target.followers.add(user)     # follow
            return Response({"detail": "Followed."})
