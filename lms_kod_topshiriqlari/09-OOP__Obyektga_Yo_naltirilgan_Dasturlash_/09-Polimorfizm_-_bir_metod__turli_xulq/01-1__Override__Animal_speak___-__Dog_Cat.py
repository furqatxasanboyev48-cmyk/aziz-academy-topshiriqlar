class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name}: ..."
class Dog(Animal):
    def speak(self):
        return f"{self.name}: woof"
class Cat(Animal):
    def speak(self):
        return f"{self.name}: meow"
kind = input().strip()
name = input().strip()
classes = {"DOG": Dog, "CAT": Cat}
if kind in classes and name:
    print(classes[kind](name).speak())
else:
    print("BAD")