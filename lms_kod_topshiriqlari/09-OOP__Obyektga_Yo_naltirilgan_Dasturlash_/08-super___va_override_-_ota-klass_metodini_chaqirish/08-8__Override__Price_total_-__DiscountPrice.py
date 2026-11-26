class Price:
    def __init__(self, qty, price):
        self.qty = qty
        self.price = price 
    def total(self):
        return self.qty * self.price
class DiscountPrice(Price):
    def total(self):
        return super().total() * 90 // 100
q, p = map(int, input().split())
print(DiscountPrice(q, p).total())