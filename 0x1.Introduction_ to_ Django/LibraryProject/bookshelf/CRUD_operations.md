from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

book = Book.objects.get(title="1984")
print(book)

book.title = "Nineteen Eighty-Four"
book.save()
print(book)

book.delete()
books = Book.objects.all()
print(books)