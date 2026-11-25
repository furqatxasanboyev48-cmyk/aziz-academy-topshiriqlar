class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors
    def info(self):
        return f"{self.brand} {self.year} doors={self.doors}"
brand = input().strip()
try:
    year = int(input().strip())
    doors = int(input().strip())
except ValueError:
    print("BAD")
else:
    if brand and 1886 <= year <= 2100 and 2 <= doors <= 6:
        print(Car(brand, year, doors).info())
    else:
        print("BAD")