class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
brand = input().strip()
try:
    year = int(input().strip())
except ValueError:
    print("BAD")
else:
    if brand and 1886 <= year <= 2100:
        car = Car(brand, year)
        print(f"CAR={car.brand} YEAR={car.year}")
    else:
        print("BAD")
        
        