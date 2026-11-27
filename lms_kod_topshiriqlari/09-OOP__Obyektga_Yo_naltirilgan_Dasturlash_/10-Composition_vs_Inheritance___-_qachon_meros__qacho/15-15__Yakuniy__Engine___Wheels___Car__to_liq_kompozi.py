class Engine:
    def __init__(self, hp):
        self.hp = hp
class Car:
    def __init__(self, hp, wheels):
        self.engine = Engine(hp)
        self.wheels = wheels
    def info(self):
        return f"{self.engine.hp} ot kuchi, {self.wheels} g'ildirak"
hp, w = map(int, input().split())    
print(Car(hp, w).info())