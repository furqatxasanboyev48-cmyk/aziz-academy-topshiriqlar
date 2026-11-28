class Book:
    def __init__(self, title, year):
        self.title = title
        self.year = year
    def __str__(self):
        return f"{self.title} ({self.year})"
    def __repr__(self):
        return f"Book(title={self.title!r}, year={self.year})"
title = input().strip()
try:
    year = int(input().strip())
except ValueError:
    print("BAD")
else:
    if title and 0 <= year <= 2100:
        b = Book(title, year)
        print(str(b))
        print(repr(b))
    else:
        print("BAD")