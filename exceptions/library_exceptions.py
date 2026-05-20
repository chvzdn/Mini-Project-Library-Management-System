# Exception classes
# Used for handling system errors

class BookNotFoundError(Exception):
    pass

class MemberNotFoundError(Exception):
    pass

class BookUnavailableError(Exception):
    pass

class LoanNotFoundError(Exception):
    pass

class BookAlreadyReturnedError(Exception):
    pass
