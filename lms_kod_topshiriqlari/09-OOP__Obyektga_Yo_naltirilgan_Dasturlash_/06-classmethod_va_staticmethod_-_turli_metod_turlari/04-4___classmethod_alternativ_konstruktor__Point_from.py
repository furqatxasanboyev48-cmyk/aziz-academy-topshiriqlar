class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    @classmethod
    def from_string(cls, s):
        a, b = s.split(",")
        return cls(int(a), int(b))
p = Point.from_string(input())
print(p.x, p.y)