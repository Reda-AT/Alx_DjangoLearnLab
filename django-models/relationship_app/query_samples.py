from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
author_name = "Author Name"  # Replace with actual author name
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

# Query 2: List all books in a library
library_name = "Library Name"  # Replace with actual library name
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

# Query 3: Retrieve the librarian for a library
librarian = Librarian.objects.get(library_name=library_name)
print(f"Librarian for {library_name}: {librarian.name}")
