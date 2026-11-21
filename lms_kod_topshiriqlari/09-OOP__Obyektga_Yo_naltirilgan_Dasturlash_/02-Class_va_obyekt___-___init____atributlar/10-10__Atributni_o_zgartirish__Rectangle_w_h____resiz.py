class Rectangle:
    def __init__(self, w, h):
        self.w = w 
        self.h = h 
    def resize(self, dw, dh):
        self.w += dw 
        self.h += dh
try:
    w = int(input().strip())
    h = int(input().strip())
    dw = int(input().strip())
    dh = int(input().strip())
except ValueError:
    print("BAD")
else:
    if w > 0 and h > 0:
        r = Rectangle(w, h)
        r.resize(dw, dh)
        if r.w > 0 and r.h > 0:
            print(f"W={r.w} H={r.h}")
        else:
            print("BAD")
    else:
        print("BAD")
        
        