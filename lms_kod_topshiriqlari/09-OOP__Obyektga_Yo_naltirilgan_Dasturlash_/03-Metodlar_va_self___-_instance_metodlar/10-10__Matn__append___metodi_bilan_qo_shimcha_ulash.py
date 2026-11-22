class Text:
    def __init__(self, base):
        self.base = base 
    def append(self, suffix):
        self.base = self.base + suffix
base = input().strip()
suffix = input().strip()
if base and suffix:
    t = Text(base)
    t.append(suffix)
    print(t.base)
else:
    print("BAD")
    
    