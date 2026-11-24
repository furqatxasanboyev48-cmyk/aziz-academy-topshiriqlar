class Circle:
    def __init__(self, r):
        self._r = r 
    @property
    def circumference(self):
        return round(2 * 3.14 * self._r, 2)
print(Circle(int(input())).circumference)    