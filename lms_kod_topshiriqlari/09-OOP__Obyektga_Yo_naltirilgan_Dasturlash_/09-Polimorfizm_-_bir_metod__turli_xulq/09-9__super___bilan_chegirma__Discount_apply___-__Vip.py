class Discount:
    def apply(self, price):
        return price
class VipDiscount(Discount):
    def apply(self, price):
        return max(0, super().apply(price) - 10)
kind = input().strip()
try:
    price = int(input().strip())
except ValueError:
    print("BAD")
else:
    classes = {"BASE": Discount, "VIP": VipDiscount}
    if kind in classes and price >= 0:
        print(classes[kind]().apply(price))
    else:
        print("BAD")