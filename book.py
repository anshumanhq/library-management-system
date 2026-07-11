#book
class Book:
    def __init__(self, title: str, author: str, isbn: str, year: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.is_borrowed = False
        self.borrowed_by = None

    def __str__(self):
        status = "Available" if not self.is_borrowed else f"Borrowed by {self.borrowed_by}"
        return f"{self.title} by {self.author} ({self.year}) - {status}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "year": self.year,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": self.borrowed_by
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(data['title'], data['author'], data['isbn'], data['year'])
        book.is_borrowed = data.get('is_borrowed', False)
        book.borrowed_by = data.get('borrowed_by', None)
        return book

    def borrow(self, user_id):
        self.is_borrowed = True
        self.borrowed_by = user_id

    def return_book(self):
        self.is_borrowed = False
        self.borrowed_by = None