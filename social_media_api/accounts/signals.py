# accounts/signals.py
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import m2m_changed
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification

User = settings.AUTH_USER_MODEL



User = settings.AUTH_USER_MODEL

@receiver(m2m_changed, sender=User.following.through)
def notify_on_follow(sender, instance, action, pk_set, **kwargs):
    # instance is the follower user
    if action == "post_add":
        for followed_pk in pk_set:
            from django.contrib.auth import get_user_model
            UserModel = get_user_model()
            followed_user = UserModel.objects.get(pk=followed_pk)
            if followed_user != instance:
                Notification.objects.create(
                    recipient=followed_user,
                    actor=instance,
                    verb="followed",
                    target_content_type=ContentType.objects.get_for_model(instance),
                    target_object_id=str(instance.pk),
                )

