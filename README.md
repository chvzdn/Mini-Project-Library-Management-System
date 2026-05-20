# Library Management System

The Library Management System is a standalone Python console-based application designed to manage basic library operations such as book registration, member management, and borrowing/returning of books.

The system provides a simple and structured way to simulate real-world library processes using Object-Oriented Programming (OOP) principles.

The application allows users to:
- Add and manage books in the library collection
- Register and manage library members
- Borrow books and track active loans
- Return borrowed books and update availability
- View all books, members, and loan records in the system

Built as a console-based application, the system focuses on simplicity, clarity, and proper separation of concerns using OOP design. It runs entirely in the terminal and does not require external databases or internet connectivity.

Through this project, users can understand how basic library operations are implemented in software systems while practicing modular programming and object-oriented design.

## Technologies Used

- Python 3 (core programming language)
- Object-Oriented Programming (OOP)
- Dictionaries for data storage
- Exception handling for error management
- Console/Terminal-based interface
  
## Project Structure

```text
library-management-system/
│
├── main.py
├── models/
│   ├── book.py
│   ├── member.py
│   └── loan.py
│
├── services/
│   ├── book_service.py
│   ├── member_service.py
│   └── loan_service.py
│
├── exceptions/
│   ├── book_exception.py
│   ├── member_exception.py
│   └── loan_exception.py
│
└── README.md
```

## How to Run

Requirements:
- Python 3.x installed

Run the program:
```bash
python main.py
```

## Sample Menu

```text
===== Library Management System =====
1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. View Books
6. View Members
7. View Loans
8. Exit
```
## Features Overview
- Add books to the system with details such as title, author, and ID
- Register library members with unique identification
- Borrow books while updating availability status
- Return books and update loan records
- View complete lists of books, members, and active loans

## Author
Developed by:
Renelyn Dino

In Partial Fulfillment of the Requirements for the Subject CC103 Computer Programming 2 Under the Course of Bachelor of Science in Information Technology at Sorsogon State University Bulan Campus. With the Supervision of our Professor John Mark Gabrentina.

## Notes

- The system is fully console-based and runs in the terminal
- Uses dictionaries for temporary data storage (no database integration)
- Exception handling is implemented for basic error control
- Focus is on OOP structure and clean code organization
- Designed as a school mini project submission
