class TextLine:
    def __init__(self, s):
        self.s = s.strip()
    def __len__(self):
        return len(self.s)
line = TextLine(input())    
print(len(line) if len(line) > 0 else "BAD")