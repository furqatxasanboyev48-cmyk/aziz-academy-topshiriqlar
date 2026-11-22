class Rectangle:
    def __init__(self, w, h):
        self.w = w 
        self.h = h 
    def area(self):
        return self.w * self.h 
try:
    w = int(input().strip())
    h = int(input().strip())
except ValueError:
    print("BAD")
else:
    if w > 0 and h > 0:
        print(Rectangle(w, h).area())
    else:
        print("BAD")
        
    