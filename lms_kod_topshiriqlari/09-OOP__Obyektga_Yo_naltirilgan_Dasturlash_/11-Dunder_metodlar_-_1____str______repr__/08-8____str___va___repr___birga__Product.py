class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name}: {self.price}"
    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"
name = input().strip()
try:
    price = int(input().strip())
except ValueError:
    print("BAD")
else:
    if name and price >= 0:
        p = Product(name, price)
        print(str(p))
        print(repr(p))
    else:
        print("BAD")