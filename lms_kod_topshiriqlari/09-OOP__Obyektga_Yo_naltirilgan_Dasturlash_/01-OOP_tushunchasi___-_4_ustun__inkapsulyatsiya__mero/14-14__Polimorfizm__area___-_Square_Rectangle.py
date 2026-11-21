class Square:
    def __init__(self, s):
        self.s = s 
    def area(self):
        return self.s * self.s 
class Rectangle:
    def __init__(self, w, h):
        self.w = w 
        self.h = h 
    def area(self):
        return self.w * self.h 
parts = input().split()
if parts[0] == "kv":
    shape = Square(int(parts[1]))
else:
    shape = Rectangle(int(parts[1]), int(parts[2]))
print(shape.area())
    
        