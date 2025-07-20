from project.print_books import Book, PaperFormatter, Printer

b = Book("Hi There! How are you?")

f = PaperFormatter()
p = Printer()
print(p.get_book(b, f))