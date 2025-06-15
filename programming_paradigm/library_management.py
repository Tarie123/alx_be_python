# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out the first available book with the given title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        # Optionally, could print "Book not available" if needed

    def return_book(self, title):
        """Returns the first book found with the given title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        # Optionally, could print "Book not found or already returned"

    def list_available_books(self):
        """Prints all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(book)
