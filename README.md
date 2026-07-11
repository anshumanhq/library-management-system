# 📚 Library Management System

A full-featured **Library Management System** built with **Python** using **Object-Oriented Programming (OOP)** principles. This project demonstrates real-world application of classes, inheritance, polymorphism, encapsulation, and file-based data persistence.

---

## 🚀 Features

- ✅ **Add, Remove, and Search Books** (by title, author, or ISBN)
- ✅ **Register Users** as `Student` or `Faculty` (with role-specific attributes)
- ✅ **Borrow and Return Books** with due date tracking
- ✅ **Automatic Fine Calculation** (₹5 per day late return)
- ✅ **JSON Data Persistence** – Data saved automatically to files
- ✅ **Menu-Driven CLI Interface** – Easy to use and test
- ✅ **ISBN Validation** (supports ISBN-10 and ISBN-13 formats)
- ✅ **OOP Principles** – Encapsulation, Inheritance, Polymorphism, Abstraction

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python 3.10+** | Core programming language |
| **OOP (Classes & Objects)** | Code organization and reusability |
| **JSON** | Data storage (books, users, transactions) |
| **Git & GitHub** | Version control |

---

## 📁 Project Structure

```
library-management-system/
│
├── main.py                # Entry point – CLI Menu
├── book.py                # Book Class
├── user.py                # User, Student, Faculty Classes
├── transaction.py         # Transaction Class
├── library.py             # Library Core Logic (Brain)
├── utils.py               # Helper Functions (ID gen, ISBN validation, File I/O)
├── data/                  # JSON data files (auto-created)
│   ├── books.json
│   ├── users.json
│   └── transactions.json
├── requirements.txt       # Python dependencies (optional)
└── README.md              # Project documentation
```

---

## 💻 How to Run

### 1. Clone the Repository
```
git clone https://github.com/YOUR_USERNAME/library-management-system.git
cd library-management-system
```

### 2. Run the Program
```
python main.py
```

### 3. Follow the Menu Options
You'll see a menu like this:

```
==================================================
        📚 LIBRARY MANAGEMENT SYSTEM
==================================================
1. Add a new book
2. Remove a book
3. Search books
4. Register a new user
5. Borrow a book
6. Return a book
7. View all books
8. View all users
9. View all transactions
10. Save data and exit
==================================================
```

---

## 🧪 Sample Usage

### Add a Book
```
Enter book title: Python Programming
Enter author name: John Doe
Enter ISBN: 978-3-16-148410-0
Enter publication year: 2020
✅ Book 'Python Programming' added successfully!
```

### Register a User
```
--- User Registration ---
Full name: Anshuman Singh
Email: anshuman@example.com
Phone: 9876543210
Membership types: 1. Student  2. Faculty
Enter 1 or 2: 1
Roll number: CS2024-01
✅ User 'Anshuman Singh' registered successfully! (ID: U001)
```

### Borrow a Book
```
Enter your User ID: U001
Enter ISBN of the book to borrow: 978-3-16-148410-0
✅ Book 'Python Programming' borrowed successfully by Anshuman Singh.
```

### Return a Book
```
Enter your User ID: U001
Enter ISBN of the book to return: 978-3-16-148410-0
✅ Book 'Python Programming' returned successfully. No fine.
```

---

## 📦 Dependencies

This project uses only Python's **standard library**. No external packages are required.

---

## 🧠 OOP Concepts Demonstrated

| Concept | Implementation |
| :--- | :--- |
| **Encapsulation** | Private attributes (`is_borrowed`, `borrowed_by`) with methods to modify them |
| **Inheritance** | `Student` and `Faculty` inheriting from `User` |
| **Polymorphism** | `Student` and `Faculty` have their own `__str__()` implementations |
| **Abstraction** | `Library` class hides complex logic (borrow/return/fine) behind simple methods |
| **Composition** | `Library` contains lists of `Book`, `User`, and `Transaction` objects |

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**Anshuman Singh**  
[GitHub](https://github.com/YOUR_USERNAME)

---

## 🙏 Acknowledgments

- Built as a practical project to strengthen Object-Oriented Programming (OOP) concepts.
- Inspired by real-world library management systems.