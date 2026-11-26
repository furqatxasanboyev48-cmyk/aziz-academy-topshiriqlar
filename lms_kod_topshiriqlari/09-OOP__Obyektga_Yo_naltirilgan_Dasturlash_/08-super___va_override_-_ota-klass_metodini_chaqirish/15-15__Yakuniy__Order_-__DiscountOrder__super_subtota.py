class Order:
    def __init__(self, qty, price):
        self.qty = qty
        self.price = price
    def subtotal(self):
        return self.qty * self.price
class DiscountOrder(Order):
    def __init__(self, qty, price, disc):
        super().__init__(qty, price)
        self.disc = disc 
    def total(self):
        st = super().subtotal()
        return st - st * self.disc // 100
q, p, d = map(int, input().split())
print(DiscountOrder(q, p, d).total())
        