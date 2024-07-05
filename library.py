class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.patrons = []

    def list_books(self):
        for book in self.books:
            print(book)

    def list_patrons(self):
        for patron in self.patrons:
            print(patron)
