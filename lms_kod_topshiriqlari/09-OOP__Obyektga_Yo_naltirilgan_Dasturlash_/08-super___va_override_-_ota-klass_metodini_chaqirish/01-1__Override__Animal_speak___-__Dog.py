class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name}: ..."
class Dog(Animal):
    def speak(self):
        return f"{self.name}: Vov"
print(Dog(input()).speak())    