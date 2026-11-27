class Item:
    def __init__(self, price):
        self.price = price
class Cart:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def total(self):
        return sum(i.price for i in self.items)
prices = list(map(int, input().split()))    
cart = Cart()
for p in prices:
    cart.add(Item(p))
print(cart.total())