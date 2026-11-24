class Circle:
    def __init__(self, r):
        self._r = r 
    @property
    def diameter(self):
        return self._r * 2
print(Circle(int(input())).diameter)