# Loan class
# Represents a borrowed book transaction

class Loan:
    def __init__(self, loan_id, book, member):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.is_active = True

    def return_book(self):
        self.is_active = False
        self.book.available = True
