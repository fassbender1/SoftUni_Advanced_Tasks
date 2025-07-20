class Book:
    def __init__(self, title, author, page = 0):
        self.title = title
        self.author = author
        self.page = page

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"Title: {self.title}, ({self.page}) pages. From author: {self.author}"

class Library:
    def __init__(self, books: list[Book]):
        self.books = books

    def find_book_by_title(self, title: str) -> Book | str:
        try:
            book = [b for b in self.books if b.title == title][0]
            return book
        except IndexError:
            return f"We do not have this book"

    def find_book_by_author(self, author: str) -> Book | str:
        try:
            book = [b for b in self.books if b.author == author][0]
            return book
        except IndexError:
            return f"We do not have this author"

