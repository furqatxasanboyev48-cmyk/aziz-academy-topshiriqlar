class Shop:
    discount = 0
    @classmethod
    def set_discount(cls, d):
        cls.discount = d 
    def __init__(self, price):
        self.price = price
    def final(self):
        return self.price - self.price * Shop.discount // 100
d, p = map(int, input().split())   
Shop.set_discount(d)
print(Shop(p).final())