class Rectangle:
    def __init__(self, w, h):
        self.w = w 
        self.h = h 
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.w + self.h)
try:
    w = int(input().strip())
    h = int(input().strip())
except ValueError:
    print("BAD")
else:
    if w > 0 and h > 0:
        r = Rectangle(w, h)
        print(f"A={r.area()}")
        print(f"P={r.perimeter()}")
    else:
        print("BAD")