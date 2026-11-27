class Address:
    def __init__(self, city):
        self.city = city
class Person:
    def __init__(self, name, city):
        self.name = name
        self.address = Address(city)
    def info(self):
        return f"{self.name} - {self.address.city}"
parts = input().split()
print(Person(parts[0], parts[1]).info())