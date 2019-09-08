class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return "{} by {}".format(self.title, self.author)
    
class Bookcase:
    def __init__(self, books=None):
        self.books = books
        
    @classmethod
    def create_bookcase(cls, book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title, author))
        return cls(books)
    
    
instance = Bookcase.create_bookcase([('book name 1', 'Author 1'), ('Book name 2', 'Author 2')])
print(instance.books[0])
print(str(instance.books[1]))