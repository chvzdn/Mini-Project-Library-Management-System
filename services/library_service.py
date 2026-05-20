from models.book import Book
from models.member import Member
from models.loan import Loan

from exceptions.library_exceptions import *

# Main service class
# Handles all library operations
class LibraryService:
    # Constructor
    def __init__(self):
        self._books = {}
        self._members = {}
        self._loans = {}

     # ===== ADD BOOK =====
    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)

        self._books[book_id] = book

        return f"Book added: {title}"

    # ===== REGISTER MEMBER =====
    def register_member(self, member_id, name, email):
        member = Member(member_id, name, email)

        self._members[member_id] = member

        return f"Member registered: {name}"

    # ===== BORROW BOOK =====
    def borrow_book(self, loan_id, book_id, member_id):
        book = self._books.get(book_id)

        if book is None:
            raise BookNotFoundError("Book not found.")

        member = self._members.get(member_id)

        if member is None:
            raise MemberNotFoundError("Member not found.")

        if not book.available:
            raise BookUnavailableError("Book already borrowed.")

        loan = Loan(loan_id, book, member)

        self._loans[loan_id] = loan

        book.available = False

        return f"{member.name} borrowed {book.title}"

    # ===== RETURN BOOK =====
    def return_book(self, loan_id):
        loan = self._loans.get(loan_id)

        if loan is None:
            raise LoanNotFoundError("Loan not found.")

        if not loan.is_active:
            raise BookAlreadyReturnedError("Book already returned.")

        loan.return_book()

        loan.book.available = True

        return f"Book '{loan.book.title}' returned successfully."

    # ===== VIEW BOOKS =====
    def view_books(self):
        return list(self._books.values())

    # ==== VIEW MEMBERS =====
    def view_members(self):
        return list(self._members.values())

    # ==== VIEW LOANS =====
    def view_loans(self):
        return list(self._loans.values())
