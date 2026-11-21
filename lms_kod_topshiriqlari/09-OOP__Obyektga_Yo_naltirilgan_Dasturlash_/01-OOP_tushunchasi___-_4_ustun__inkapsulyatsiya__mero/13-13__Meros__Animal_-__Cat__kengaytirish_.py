class Animal:
    def __init__(self, name):
        self.name = name
class Cat(Animal):
    def sound(self):
        return f"{self.name}: Myau"
print(Cat(input()).sound())