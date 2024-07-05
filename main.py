from book import Book
from library import Library
from patron import Patron
from librarian import Librarian

lib = Library('Wseiz Library')

book1 = Book('Robinson Crusoe', 'Daniel Defoe', '978-0-14-143982-2')
book2 = Book('Harry Potter', 'J.K. Rowling', '978-0-7475-3269-9')

librarian = Librarian('Alice', 'L001')
librarian.add_book(lib, book1)
librarian.add_book(lib, book2)

patron1 = Patron('Bob', 'P001')
librarian.add_patron(lib, patron1)

lib.list_books()
lib.list_patrons()

patron1.borrow_book(book1)
lib.list_books()
