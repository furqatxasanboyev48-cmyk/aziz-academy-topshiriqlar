class Fraction:
    def __init__(self, a, b):
        self.a = a 
        self.b = b 
    def __repr__(self):
        return f"Fraction(a={self.a}, b={self.b})"
try:
    a = int(input().strip())
    b = int(input().strip())
except ValueError:
    print("BAD")
else:
    if b != 0:
        print(repr(Fraction(a, b)))
    else:
        print("BAD")