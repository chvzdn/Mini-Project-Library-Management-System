from services.library_service import LibraryService
from exceptions.library_exceptions import *

service = LibraryService()


# Function to display the menu
def menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")


# Main program loop
while True:
    menu()
     # Ask user for menu choice
    choice = input("Enter choice: ")

    try:
        # ===== ADD BOOK =====
        if choice == "1":
            # Ask user for book details
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")

            print(service.add_book(book_id, title, author))

        # ===== REGISTER MEMBER =====
        elif choice == "2":
            # Ask user for member details
            member_id = input("Member ID: ")
            name = input("Name: ")
            email = input("Email: ")

            print(service.register_member(member_id, name, email))

        # ===== BORROW BOOK =====
        elif choice == "3":
            # Ask user for borrowing details
            loan_id = input("Loan ID: ")
            book_id = input("Book ID: ")
            member_id = input("Member ID: ")

            print(service.borrow_book(loan_id, book_id, member_id))

        # ===== RETURN BOOK =====
        elif choice == "4":
            # Ask user for loan ID to return book
            loan_id = input("Loan ID: ")

            print(service.return_book(loan_id))

        # ===== VIEW BOOKS =====
        elif choice == "5":
            # Get list of books
            books = service.view_books()

            # Check if there are no books
            if not books:
                print("No books found.")
            else:
                print("\nBooks:")
                # Display each book
                for book in books:
                    # Check availability
                    status = "Available" if book.available else "Borrowed"
                    print(f"{book.book_id} | {book.title} | {book.author} | {status}")

        #==== VIEW MEMBERS =====
        elif choice == "6":
            # Get list of members
            members = service.view_members()

            if not members:
                print("No members found.")
            else:
                print("\nMembers:")
                # Display all members
                for member in members:
                    print(f"{member.member_id} | {member.name} | {member.email}")

        # ==== VIEW LOANS =====
        elif choice == "7":
            # Get all loans
            loans = service.view_loans()

            if not loans:
                print("No loans found.")
            else:
                print("\nLoans:")
                for loan in loans:
                    # Check loan status
                    status = "Active" if loan.is_active else "Closed"
                    print(
                        f"{loan.loan_id} | "
                        f"{loan.member.name} borrowed "
                        f"{loan.book.title} | {status}"
                    )

        # ==== EXIT PROGRAM =====
        elif choice == "8":
            print("Program closed.")
            break

        # Invalid menu choice
        else:
            print("Invalid choice.")

    # Handle possible exception errors
    except Exception as e:
        print(f"Error: {e}")
