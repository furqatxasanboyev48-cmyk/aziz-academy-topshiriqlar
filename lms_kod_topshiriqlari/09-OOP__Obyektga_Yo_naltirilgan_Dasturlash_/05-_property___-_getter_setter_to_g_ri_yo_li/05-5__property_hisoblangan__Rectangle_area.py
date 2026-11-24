class Rectangle:
    def __init__(self, w, h):
        self._w = w 
        self._h = h 
    @property
    def area(self):
        return self._w * self._h 
w, h = map(int, input().split()) 
print(Rectangle(w, h).area)
        