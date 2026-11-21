class Product:
    def __init__(self, name, price, qty):
        self.name = name 
        self.price = price
        self.qty = qty
    def total(self):
        return self.price * self.qty
name = input().strip()
try:
    price = int(input().strip())
    qty = int(input().strip())
except ValueError:
    print("BAD")
else:
    if name and price >= 0 and qty >= 0:
        print(Product(name, price, qty).total())
    else:
        print("BAD")