class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class EBook(Book):
    def __init__(self, title, author, file_size_mb):
        super().__init__(title, author)
        self.file_size_mb = file_size_mb
    def display(self):
        print(f"EBook: '{self.title}' by {self.author} [{self.file_size_mb} MB]")
digital_book = EBook("Learn Python", "Mark Lutz", 5.2)
digital_book.display()
