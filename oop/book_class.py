# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor: Initializes the book with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the book object is deleted."""
        print(f"Deleting '{self.title}'")

    def __str__(self):
        """String representation: User-friendly description of the book."""
        return f"'{self.title}' by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation: Code-like string that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"



if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    print(str(book1))     
    print(repr(book1))    

    del book1
