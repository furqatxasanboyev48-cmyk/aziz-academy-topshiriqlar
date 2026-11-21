class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
try:
    x = int(input().strip())
    y = int(input().strip())
except ValueError:
    print("BAD")
else:
    p = Point(x, y)
    print(f"X={p.x} Y={p.y}")