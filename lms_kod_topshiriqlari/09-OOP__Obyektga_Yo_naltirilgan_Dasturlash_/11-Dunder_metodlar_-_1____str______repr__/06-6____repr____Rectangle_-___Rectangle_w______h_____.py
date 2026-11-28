class Rectangle:
    def __init__(self, w, h):
        self.w = w 
        self.h = h 
    def __repr__(self):
        return f"Rectangle(w={self.w}, h={self.h})"
try:
    w = int(input().strip())
    h = int(input().strip())
except ValueError:
    print("BAD")
else:
    if w > 0 and h > 0:
        print(repr(Rectangle(w, h)))
    else:
        print("BAD")