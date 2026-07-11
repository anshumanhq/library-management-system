#library
from utils import load_data, save_data, validate_isbn, get_current_date
from book import Book
from user import User, Student, Faculty
from transaction import Transaction

class Library:
    def __init__(self):
        self.books = []          # List of Book objects
        self.users = []          # List of User objects
        self.transactions = []   # List of Transaction objects
        self.load_data()

    # ---------- BOOK OPERATIONS ----------
    def add_book(self, title, author, isbn, year):
        if not validate_isbn(isbn):
            raise ValueError("ISBN is not valid")
        
        # Check if book already exists
        for book in self.books:
            if book.isbn == isbn:
                return f"❌ Book with ISBN {isbn} already exists."
        
        new_book = Book(title, author, isbn, year)
        self.books.append(new_book)
        self.save_data()
        return f"✅ Book '{title}' added successfully!"

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    return f"❌ Book '{book.title}' is currently borrowed. Cannot remove."
                self.books.remove(book)
                self.save_data()
                return f"✅ Book '{book.title}' removed successfully."
        return f"❌ Book with ISBN {isbn} not found."

    def search_books(self, query):
        query = query.lower()
        results = []
        for book in self.books:
            if query in book.title.lower() or query in book.author.lower():
                results.append(book)
        return results

    def get_all_books(self):
        return self.books

    # ---------- USER OPERATIONS ----------
    def register_user(self, user):
        # Check if user already exists (by email)
        for u in self.users:
            if u.email == user.email:
                return f"❌ User with email {user.email} already exists."
        self.users.append(user)
        self.save_data()
        return f"✅ User '{user.name}' registered successfully! (ID: {user.user_id})"

    def get_all_users(self):
        return self.users

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    # ---------- TRANSACTION OPERATIONS ----------
    def borrow_book(self, user_id, isbn):
        user = self.find_user(user_id)
        if not user:
            return f"❌ User with ID {user_id} not found."

        book = self.find_book(isbn)
        if not book:
            return f"❌ Book with ISBN {isbn} not found."

        if book.is_borrowed:
            return f"❌ Book '{book.title}' is already borrowed."

        # Create transaction
        borrow_date = get_current_date()
        transaction = Transaction(book.isbn, user.user_id, borrow_date)
        self.transactions.append(transaction)

        # Update book status
        book.borrow(user.user_id)

        self.save_data()
        return f"✅ Book '{book.title}' borrowed successfully by {user.name}."

    def return_book(self, user_id, isbn):
        user = self.find_user(user_id)
        if not user:
            return f"❌ User with ID {user_id} not found."

        book = self.find_book(isbn)
        if not book:
            return f"❌ Book with ISBN {isbn} not found."

        if not book.is_borrowed or book.borrowed_by != user_id:
            return f"❌ Book '{book.title}' was not borrowed by this user."

        # Find open transaction
        open_trans = None
        for trans in self.transactions:
            if trans.book_isbn == isbn and trans.user_id == user_id and trans.return_date is None:
                open_trans = trans
                break

        if not open_trans:
            return f"❌ No open transaction found for this book and user."

        # Close transaction
        return_date = get_current_date()
        open_trans.close_transaction(return_date)

        # Calculate fine (due date = borrow_date + 14 days)
        from datetime import datetime, timedelta
        due_date = (datetime.strptime(open_trans.borrow_date, "%Y-%m-%d") + timedelta(days=14)).strftime("%Y-%m-%d")
        fine = open_trans.calculate_fine(due_date, return_date)
        open_trans.fine = fine

        # Update book status
        book.return_book()

        self.save_data()

        if fine > 0:
            return f"✅ Book '{book.title}' returned. Late fine: ₹{fine}"
        return f"✅ Book '{book.title}' returned successfully. No fine."

    def get_all_transactions(self):
        return self.transactions

    # ---------- DATA PERSISTENCE ----------
    def save_data(self):
        # Save books
        books_data = [book.to_dict() for book in self.books]
        save_data("data/books.json", books_data)

        # Save users
        users_data = [user.to_dict() for user in self.users]
        save_data("data/users.json", users_data)

        # Save transactions
        trans_data = [trans.to_dict() for trans in self.transactions]
        save_data("data/transactions.json", trans_data)

    def load_data(self):
        # Load books
        books_data = load_data("data/books.json")
        self.books = [Book.from_dict(data) for data in books_data]

        # Load users
        users_data = load_data("data/users.json")
        self.users = [User.from_dict(data) for data in users_data]

        # Load transactions
        trans_data = load_data("data/transactions.json")
        self.transactions = [Transaction.from_dict(data) for data in trans_data]