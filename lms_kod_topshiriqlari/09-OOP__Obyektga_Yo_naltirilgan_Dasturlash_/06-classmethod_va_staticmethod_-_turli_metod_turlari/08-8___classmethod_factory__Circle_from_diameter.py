class Circle:
    def __init__(self, r):
        self.r = r 
    @classmethod
    def from_diameter(cls, d):
        return cls(d / 2)
    def area(self):
        return round(3.14 * self.r * self.r, 2)
d = int(input()) 
print(Circle.from_diameter(d).area())