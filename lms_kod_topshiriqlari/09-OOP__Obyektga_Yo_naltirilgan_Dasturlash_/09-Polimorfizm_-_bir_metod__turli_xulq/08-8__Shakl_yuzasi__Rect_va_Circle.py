class Shape:
    def area(self):
        raise NotImplementedError
class Rect(Shape):
    def __init__(self, w, h):
        self.w = w 
        self.h = h 
    def area(self):
        return self.w * self.h 
class Circle(Shape):
    def __init__(self, r):
        self.r = r 
    def area(self):
        return int(3.14 * self.r * self.r)
kind = input().strip()
try:
    a = int(input().strip())
    b = int(input().strip())
except ValueError:
    print("BAD")
else:
    if kind == "RECT" and a > 0 and b > 0:
        print(Rect(a, b).area())
    elif kind == "CIRCLE" and a > 0:
        print(Circle(a).area())
    else:
        print("BAD")
             