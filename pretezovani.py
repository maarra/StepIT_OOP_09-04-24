# magické operátory
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def showInfo(self):
        print (f'Title: {self.title} Author: {self.author} Pages: {self.pages}')

    def __str__(self):
        return (f'Title: {self.title} Author: {self.author} Pages: {self.pages}')

    def __add__(self, other):
        return f'Total pages: {self.pages + other.pages}'

book1 = Book('Python Crash Course', 'Eric Matthes', 624)
book2 = Book('JavaScript: The Good Parts', 'Douglas Crockford', 170)
book3 = Book('Název knihy', 'Autor', 100)
book4 = Book('Název knihy', 'Autor', 100)
print(book1 + book4)

print(book1)
book1.showInfo()

