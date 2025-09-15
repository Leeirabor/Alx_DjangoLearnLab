from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book

class Command(BaseCommand):
    help = "Create default groups and assign permissions"

    def handle(self, *args, **kwargs):
        # Define groups
        editors, _ = Group.objects.get_or_create(name="Editors")
        viewers, _ = Group.objects.get_or_create(name="Viewers")
        admins, _ = Group.objects.get_or_create(name="Admins")

        # Get permissions
        can_view = Permission.objects.get(codename="can_view")
        can_create = Permission.objects.get(codename="can_create")
        can_edit = Permission.objects.get(codename="can_edit")
        can_delete = Permission.objects.get(codename="can_delete")

        # Assign permissions
        editors.permissions.set([can_view, can_create, can_edit])
        viewers.permissions.set([can_view])
        admins.permissions.set([can_view, can_create, can_edit, can_delete])

        self.stdout.write(self.style.SUCCESS("Groups and permissions created successfully!"))
