class Shipping:
    def cost(self, weight):
        return weight * 10
class ExpressShipping(Shipping):
    def cost(self, weight):
        return super().cost(weight) + 50
kind = input().strip()
try:
    weight = int(input().strip())
except ValueError:
    print("BAD")
else:
    classes = {"BASE": Shipping, "EXP": ExpressShipping}
    if kind in classes and weight > 0:
        print(classes[kind]().cost(weight))
    else:
        print("BAD")