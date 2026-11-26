class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w 
        self.h = h 
    def area(self):
        return self.w * self.h 
w, h = map(int, input().split())    
print(Rectangle(w, h).area())    