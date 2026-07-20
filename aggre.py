#Agrregation
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_book(self):
        return [f"{book.title} by {book.author}" for book in self.books]


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("\n ___Entebbe Public Library___")

book1 = Book("JJK", "Gege Akutami")
book2 = Book("AOT", "Isyhama")
book3 = Book("CBVG", "Jojo")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)

for book in library.list_book():
    print(book)