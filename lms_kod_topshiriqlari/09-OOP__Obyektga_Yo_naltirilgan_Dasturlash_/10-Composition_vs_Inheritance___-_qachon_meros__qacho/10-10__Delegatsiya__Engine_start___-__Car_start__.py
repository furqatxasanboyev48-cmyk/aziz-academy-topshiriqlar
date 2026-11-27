name = input()
class Engine:
    def start(self):
        return "Motor ishladi"
class Car:
    def __init__(self, name):
        self.name = name
        self.engine = Engine()
    def start(self):
        return f"{self.name}: " + self.engine.start()
print(Car(name).start())    