class Author:
    def __init__(self, name):
        self.name = name
class Book:
    def __init__(self, title, author_name):
        self.title = title
        self.author = Author(author_name)
    def info(self):
        return f"{self.title} ({self.author.name})"
parts = input().split()
print(Book(parts[1], parts[0]).info())