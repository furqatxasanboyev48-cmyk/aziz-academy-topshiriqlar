class Vehicle:
    def __init__(self, brand):
        self.brand = brand
class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors
    def info(self):
        return f"{self.brand}: {self.doors} eshik"
parts = input().split()
print(Car(parts[0], int(parts[1])).info())
