class Word:
    def __init__(self, text):
        self.text = text 
    def __lt__(self, other):
        return len(self.text) < len(other.text)
a = input().strip()
b = input().strip()
if a and b:
    print("LT" if Word(a) < Word(b) else "GE")
else:
    print("BAD")