from project.books import Book
from project.books import Library

b1 = Book("To Kill a Mockingbird", "Author", 400)
b2 = Book("Harry Potter 5", "J. Austin", 800)
b3 = Book("Test", "Test", 20)

library = Library([b1, b2, b3])
print(library.find_book_by_title("To Kill a Mockingbird"))