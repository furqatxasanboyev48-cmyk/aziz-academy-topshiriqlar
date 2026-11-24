class Product:
    def __init__(self, price):
        self._price = price
    def set_price(self, x):
        if x >= 0:
            self._price = x 
            return True
        return False
    def get_price(self):
        return self._price
try:
    price = int(input().strip())
    new_price = int(input().strip())
except ValueError:
    print("BAD")
else:
    if price >= 0:
        p = Product(price)
        print(f"PRICE={p.get_price()}" if p.set_price(new_price) else "BAD")
    else:
        print("BAD")