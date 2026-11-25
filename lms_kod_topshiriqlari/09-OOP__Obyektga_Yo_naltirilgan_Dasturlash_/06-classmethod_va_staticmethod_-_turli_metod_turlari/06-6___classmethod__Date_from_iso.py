class Date:
    def __init__(self, y, m, d):
        self.y = y 
        self.m = m
        self.d = d 
    @classmethod
    def from_iso(cls, s):
        y, m, d = s.split("-")
        return cls(y, m, d)
    def show(self):
        return f"{self.d}.{self.m}.{self.y}"
print(Date.from_iso(input()).show())    