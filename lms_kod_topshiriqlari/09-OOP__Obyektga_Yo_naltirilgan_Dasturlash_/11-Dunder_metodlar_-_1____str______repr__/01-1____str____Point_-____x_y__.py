class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def __str__(self):
        return f"({self.x},{self.y})"
try:
    x = int(input().strip())
    y = int(input().strip())
except ValueError:
    print("BAD")
else:
    print(Point(x, y))