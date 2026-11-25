class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):   
    def bark(self):
        return f"{self.name}: woof"
name = input().strip()
if name:
    print(Dog(name).bark())
else:
    print("BAD")