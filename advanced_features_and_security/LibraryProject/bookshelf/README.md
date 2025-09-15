# Permissions and Groups Setup

## Custom Permissions
The `Book` model has the following custom permissions:
- `can_view` → Allows viewing books
- `can_create` → Allows creating new books
- `can_edit` → Allows editing existing books
- `can_delete` → Allows deleting books

## Groups
- **Editors** → `can_view`, `can_create`, `can_edit`
- **Viewers** → `can_view`
- **Admins** → `can_view`, `can_create`, `can_edit`, `can_delete`

## Usage
1. Run migrations to apply permissions:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
