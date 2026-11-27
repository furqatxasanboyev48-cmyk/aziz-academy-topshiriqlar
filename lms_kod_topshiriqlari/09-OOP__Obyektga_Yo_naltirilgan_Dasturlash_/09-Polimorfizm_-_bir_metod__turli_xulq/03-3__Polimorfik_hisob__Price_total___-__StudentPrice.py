class Price:
    def __init__(self, price):
        self.price = price
    def total(self):
        return self.price 
class StudentPrice(Price):
    def total(self):
             return int(super().total() * 0.8)
kind = input().strip()
try:
    price = int(input().strip())
except ValueError:
    print("BAD")
else:
    classes = {"BASE": Price, "STUDENT": StudentPrice}
    if kind in classes and price >= 0:
        print(classes[kind](price).total())
    else:
        print("BAD")