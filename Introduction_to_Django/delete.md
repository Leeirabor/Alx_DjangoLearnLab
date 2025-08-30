
---

## 4. **delete.md**
```markdown
# Delete a Book

To delete a book record:

```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.delete()
