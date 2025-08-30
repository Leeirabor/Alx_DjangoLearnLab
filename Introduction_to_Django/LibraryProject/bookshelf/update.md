
---

## 3. **update.md**
```markdown
# Update a Book

To update a book record:

```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

print(book)  # Expected: Nineteen Eighty-Four by George Orwell (1949)
