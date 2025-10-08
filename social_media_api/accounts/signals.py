# accounts/signals.py
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

User = settings.AUTH_USER_MODEL

@receiver(post_save)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    from django.contrib.auth import get_user_model
    if created and sender == get_user_model():
        Token.objects.create(user=instance)
