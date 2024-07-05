from person import Person

class Patron(Person):
    def __init__(self, name, patron_id):
        super().__init__(name, patron_id)
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False

    def __str__(self):
        return f"{self.name} (ID: {self.person_id}), Borrowed books: {[book.title for book in self.borrowed_books]}"
