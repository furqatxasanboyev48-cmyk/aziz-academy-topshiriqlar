class Engine:
    def __init__(self, hp):
        self.hp = hp
class Car:
    def __init__(self, hp):
        self.engine = Engine(hp)
    def power(self):
        return self.engine.hp
print(Car(int(input())).power())    