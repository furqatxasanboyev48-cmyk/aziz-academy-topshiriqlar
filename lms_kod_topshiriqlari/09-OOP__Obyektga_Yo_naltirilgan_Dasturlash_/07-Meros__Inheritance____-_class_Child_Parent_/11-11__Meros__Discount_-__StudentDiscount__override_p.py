class Discount:
    def total(self, price):
        return price
class StudentDiscount(Discount):
    def total(self, price):
        return price * 0.8
kind = input().strip()    
try:
    price = int(input().strip())
except ValueError:
    print("BAD")
else:
    classes = {"BASE": Discount, "STUDENT": StudentDiscount}
    if kind in classes and price >= 0:
        print(int(classes[kind]().total(price)))
    else:
        print("BAD")
        