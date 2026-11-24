class Temp:
    def __init__(self, c):
        self._c = c 
    @property
    def fahrenheit(self):
        return round(self._c * 9 / 5 + 32, 1)
print(Temp(int(input())).fahrenheit)
        