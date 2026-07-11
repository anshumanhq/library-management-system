# main.py
# Entry point for the Library Management System

import sys
from library import Library
from book import Book
from user import Student, Faculty
#from utils import display_menu, get_valid_input

def main():
    # Create a Library instance (this loads data automatically)
    lib = Library()
    
    while True:
        print("\n" + "="*50)
        print("        📚 LIBRARY MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add a new book")
        print("2. Remove a book")
        print("3. Search books")
        print("4. Register a new user")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. View all books")
        print("8. View all users")
        print("9. View all transactions")
        print("10. Save data and exit")
        print("="*50)
        
        choice = input("Enter your choice (1-10): ").strip()
        
        if choice == "1":
            # Add Book
            title = input("Enter book title: ").strip()
            if not title:
                print("❌ Title cannot be empty.")
                continue
            author = input("Enter author name: ").strip()
            if not author:
                print("❌ Author cannot be empty.")
                continue
            isbn = input("Enter ISBN: ").strip()
            if not isbn:
                print("❌ ISBN cannot be empty.")
                continue
            try:
                year = int(input("Enter publication year: ").strip())
            except ValueError:
                print("❌ Year must be a number.")
                continue
            result = lib.add_book(title, author, isbn, year)
            print(result)
        
        elif choice == "2":
            # Remove Book
            isbn = input("Enter ISBN of the book to remove: ").strip()
            if not isbn:
                print("❌ ISBN cannot be empty.")
                continue
            result = lib.remove_book(isbn)
            print(result)
        
        elif choice == "3":
            # Search Books
            query = input("Enter title or author keyword to search: ").strip()
            if not query:
                print("❌ Search query cannot be empty.")
                continue
            results = lib.search_books(query)
            if not results:
                print("📭 No books found matching your query.")
            else:
                print(f"\n📖 Found {len(results)} book(s):")
                for book in results:
                    print(f"  - {book}")
        
        elif choice == "4":
            # Register User
            print("\n--- User Registration ---")
            name = input("Full name: ").strip()
            if not name:
                print("❌ Name cannot be empty.")
                continue
            email = input("Email: ").strip()
            if not email:
                print("❌ Email cannot be empty.")
                continue
            phone = input("Phone number: ").strip()
            if not phone:
                print("❌ Phone cannot be empty.")
                continue
            print("Membership types: 1. Student  2. Faculty")
            mem_type = input("Enter 1 or 2: ").strip()
            if mem_type == "1":
                roll = input("Roll number: ").strip()
                if not roll:
                    print("❌ Roll number cannot be empty.")
                    continue
                user = Student(name, email, phone, roll)
            elif mem_type == "2":
                dept = input("Department: ").strip()
                if not dept:
                    print("❌ Department cannot be empty.")
                    continue
                user = Faculty(name, email, phone, dept)
            else:
                print("❌ Invalid membership type.")
                continue
            result = lib.register_user(user)
            print(result)
        
        elif choice == "5":
            # Borrow Book
            user_id = input("Enter your User ID: ").strip()
            if not user_id:
                print("❌ User ID cannot be empty.")
                continue
            isbn = input("Enter ISBN of the book to borrow: ").strip()
            if not isbn:
                print("❌ ISBN cannot be empty.")
                continue
            result = lib.borrow_book(user_id, isbn)
            print(result)
        
        elif choice == "6":
            # Return Book
            user_id = input("Enter your User ID: ").strip()
            if not user_id:
                print("❌ User ID cannot be empty.")
                continue
            isbn = input("Enter ISBN of the book to return: ").strip()
            if not isbn:
                print("❌ ISBN cannot be empty.")
                continue
            result = lib.return_book(user_id, isbn)
            print(result)
        
        elif choice == "7":
            # View all books
            books = lib.get_all_books()
            if not books:
                print("📭 No books in the library.")
            else:
                print(f"\n📚 Total books: {len(books)}")
                for book in books:
                    status = "Available" if not book.is_borrowed else f"Borrowed by {book.borrowed_by}"
                    print(f"  - {book.title} by {book.author} (ISBN: {book.isbn}) [{status}]")
        
        elif choice == "8":
            # View all users
            users = lib.get_all_users()
            if not users:
                print("📭 No users registered.")
            else:
                print(f"\n👥 Total users: {len(users)}")
                for user in users:
                    print(f"  - {user}")
        
        elif choice == "9":
            # View all transactions
            transactions = lib.get_all_transactions()
            if not transactions:
                print("📭 No transactions yet.")
            else:
                print(f"\n📋 Total transactions: {len(transactions)}")
                for trans in transactions:
                    print(f"  - {trans}")
        
        elif choice == "10":
            # Save and exit
            lib.save_data()
            print("💾 Data saved successfully. Goodbye!")
            sys.exit(0)
        
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 10.")

if __name__ == "__main__":
    main() 
