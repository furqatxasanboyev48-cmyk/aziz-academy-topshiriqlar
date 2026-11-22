class Pair:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def swap(self):
        self.x, self.y = self.y, self.x 
try:
    x = int(input().strip())
    y = int(input().strip())
except ValueError:
    print("BAD")
else:
    p = Pair(x, y)
    p.swap()
    print(f"X={p.x} Y={p.y}")