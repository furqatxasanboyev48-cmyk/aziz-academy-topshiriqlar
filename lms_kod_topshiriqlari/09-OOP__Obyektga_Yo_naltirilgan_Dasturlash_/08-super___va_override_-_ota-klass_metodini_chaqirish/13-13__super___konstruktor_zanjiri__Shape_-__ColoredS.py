class Shape:
    def __init__(self, side):
        self.side = side
class ColoredShape(Shape):
    def __init__(self, color, side):
        super().__init__(side)
        self.color = color 
    def info(self):
        return f"{self.color} {self.side}x{self.side}"
parts = input().split()
print(ColoredShape(parts[0], int(parts[1])).info())