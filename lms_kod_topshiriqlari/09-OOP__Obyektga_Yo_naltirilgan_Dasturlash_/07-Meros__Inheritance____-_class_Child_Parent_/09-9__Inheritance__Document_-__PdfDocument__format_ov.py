class Document:
    def __init__(self, title):
        self.title = title
    def describe(self):
        return f"DOC:{self.title}"
class PdfDocument(Document):
    def __init__(self, title, pages):
        super().__init__(title)
        self.pages = pages
    def describe(self):
        return f"PDF:{self.title} pages={self.pages}"
title = input().strip()
try:
    pages = int(input().strip())
except ValueError:
    print("BAD")
else:
    if title and pages > 0:
        print(PdfDocument(title, pages).describe())
    else:
        print("BAD")