from utils import generate_id
from datetime import datetime

class Transaction:
    def __init__(self, book_isbn, user_id, borrow_date):
        self.transaction_id = generate_id("T")
        self.book_isbn = book_isbn
        self.user_id = user_id
        self.borrow_date = borrow_date
        self.return_date = None
        self.fine = 0

    def close_transaction(self, return_date):
        self.return_date = return_date

    def calculate_fine(self, due_date, return_date):
        fine_per_day = 5
        fmt = "%Y-%m-%d"
        fine_days = (datetime.strptime(return_date, fmt) - datetime.strptime(due_date, fmt)).days
        return max(0, fine_days * fine_per_day)

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "book_isbn": self.book_isbn,
            "user_id": self.user_id,
            "borrow_date": self.borrow_date,
            "return_date": self.return_date,
            "fine": self.fine
        }

    @classmethod
    def from_dict(cls, data):
        trans = cls(data['book_isbn'], data['user_id'], data['borrow_date'])
        trans.transaction_id = data['transaction_id']
        trans.return_date = data.get('return_date')
        trans.fine = data.get('fine', 0)
        return trans