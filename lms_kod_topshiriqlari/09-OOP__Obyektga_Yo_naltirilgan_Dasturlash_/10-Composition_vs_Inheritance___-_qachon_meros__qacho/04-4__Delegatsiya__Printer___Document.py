class Document:
    def __init__(self, text):
        self.text = text
class Printer:
    def print_doc(self, doc):
        return doc.text.upper()
d = Document(input())   
print(Printer().print_doc(d))
        