class Product:
    def __init__(self):
        self._price = 0
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, v):
        if v >= 0:
            self._price = v 
p = Product()
p.price = int(input())
print(p.price)