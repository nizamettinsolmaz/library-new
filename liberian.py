from person import Person

class Librarian(Person):
    def __init__(self, name, librarian_id):
        super().__init__(name, librarian_id)

    def add_book(self, library, book):
        library.books.append(book)

    def add_patron(self, library, patron):
        library.patrons.append(patron)
