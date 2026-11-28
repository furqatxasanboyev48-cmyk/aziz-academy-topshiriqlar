class Fraction:
    def __init__(self, a, b):
        self.a = a 
        self.b = b 
    def __str__(self):
        return f"{self.a}/{self.b}"
try:
    a = int(input().strip())
    b = int(input().strip())
except ValueError:
    print("BAD")
else:
    if b != 0:
        print(Fraction(a, b))
    else:
        print("BAD")