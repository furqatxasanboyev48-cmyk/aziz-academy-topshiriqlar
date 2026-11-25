class Temperature:
    def __init__(self, c):
        self.c = c 
    @staticmethod
    def _to_f(c):
        return c * 9 / 5 + 32
    def fahrenheit(self):
        return round(self._to_f(self.c), 1)
print(Temperature(int(input())).fahrenheit())   