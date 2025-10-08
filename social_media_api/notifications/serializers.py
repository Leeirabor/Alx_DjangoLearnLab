# notifications/serializers.py
from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    # we can show a minimal representation of target:
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ("id", "recipient", "actor", "verb", "target", "unread", "timestamp")
        read_only_fields = ("id", "actor", "recipient", "verb", "target", "timestamp")

    def get_target(self, obj):
        if not obj.target:
            return None
        return {
            "type": obj.target_content_type.model,
            "id": str(obj.target_object_id),
            "repr": str(obj.target)
        }
