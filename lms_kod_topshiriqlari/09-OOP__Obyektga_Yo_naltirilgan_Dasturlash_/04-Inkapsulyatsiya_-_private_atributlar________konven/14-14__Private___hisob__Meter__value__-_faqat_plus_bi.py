class Meter:
    def __init__(self, start):
        self._value = start 
    def plus(self, x):
        if x > 0:
            self._value += x 
            return True
        return False
    def value(self):
        return self._value
try:
    start = int(input().strip())
    add = int(input().strip())
except ValueError:
    print("BAD")
else:
    if start >= 0:
        m = Meter(start)
        print(m.value() if m.plus(add) else "BAD")
    else:
        print("BAD")
            