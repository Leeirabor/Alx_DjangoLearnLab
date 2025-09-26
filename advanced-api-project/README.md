# Advanced API Project - Django REST Framework

## Overview
This project demonstrates the use of Django REST Framework (DRF) generic views and permissions to build a structured API.

## Endpoints
- `GET /api/books/` → List all books (public)
- `GET /api/books/<id>/` → Retrieve a single book (public)
- `POST /api/books/create/` → Create a book (authenticated only)
- `PUT /api/books/<id>/update/` → Update a book (authenticated only)
- `DELETE /api/books/<id>/delete/` → Delete a book (authenticated only)

## Permissions
- **Anonymous users**: Read-only access (list & detail views).
- **Authenticated users**: Full access (create, update, delete).

## Notes
- Custom `perform_create` and `perform_update` hooks allow for extended logic (e.g., auto-assign author, logging, validation).
- Permissions are enforced via DRF’s `IsAuthenticated` and `AllowAny` classes.
