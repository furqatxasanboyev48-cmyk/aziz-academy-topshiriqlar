class Base:
    def __init__(self, x):
        self.x = x 
    def value(self):
        return self.x 
class Child(Base):
    def value(self):
        return super().value() * 2
kind = input().strip()
try:
    x = int(input().strip())
except ValueError:
    print("BAD")
else:
    classes = {"BASE": Base, "CHILD": Child}
    if kind in classes:
        print(classes[kind](x).value())
    else:
        print("BAD")