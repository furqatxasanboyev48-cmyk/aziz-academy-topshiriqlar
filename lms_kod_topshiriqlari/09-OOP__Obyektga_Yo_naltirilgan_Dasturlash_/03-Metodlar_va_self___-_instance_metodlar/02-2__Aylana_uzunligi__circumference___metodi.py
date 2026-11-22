class Circle:
    def __init__(self,r):
        self.r = r 
    def circumference(self):
        return int(2 * 3.14 * self.r)
try:
    r = int(input().strip())
except ValueError:
    print("BAD")
else:
    if r > 0:
        print(Circle(r).circumference())
    else:
        print("BAD")
        