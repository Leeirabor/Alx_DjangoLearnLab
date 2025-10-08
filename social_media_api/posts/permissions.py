# posts/permissions.py
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Allow safe (read-only) methods for everyone.
    Only the author may update/delete an object.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only methods are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the author
        return obj.author == request.user
