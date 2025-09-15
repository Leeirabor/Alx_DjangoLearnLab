
---

## 2. **retrieve.md**
```markdown
# Retrieve Books

To fetch all books:

```python
from bookshelf.models import Book

books = Book.objects.all()
print(books)  # Expected: <QuerySet [<Book: 1984 by George Orwell (1949)>]>

# get a single book
from bookshelf.models import Book

book = Book.objects.get(id=1)
print(book)
# Expected output:
# 1984 by George Orwell (1949)