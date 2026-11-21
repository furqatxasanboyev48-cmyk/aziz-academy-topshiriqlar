class Circle:
    def __init__(self, r):
        self.r = r 
    def area(self):
        return round(3.14 * self.r * self.r, 2)
print(Circle(int(input())).area())