class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  
        return False

    def return_book(self):
        if not self._is_checked_out:
            self._is_checked_out = False
            return False  
        return True
    
    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = {}

    def add_book(self, book):
        self._books[book.title] = book

    def check_out_book(self, title):
        if title in self._books:
            book = self._books[title]
            if book.check_out():
                return f"You have checked out '{title}'."
            else:
                return f"'{title}' is currently checked out."
        return f"'{title}' not found in the library."

    def return_book(self, title):
        if title in self._books:
            book = self._books[title]
            if book.return_book():
                return f"You have returned '{title}'."
            else:
                return f"'{title}' was not checked out."
        return f"'{title}' not found in the library."

    def list_available_books(self):
        available_books = [title for title, book in self._books.items() if book.is_available()]
        return available_books if available_books else "No books are available."
