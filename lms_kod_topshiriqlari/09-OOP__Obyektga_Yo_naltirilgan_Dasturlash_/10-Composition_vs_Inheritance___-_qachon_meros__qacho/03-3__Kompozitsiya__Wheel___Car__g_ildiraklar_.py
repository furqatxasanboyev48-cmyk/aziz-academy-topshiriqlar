class Wheel:
    pass
class Car:
    def __init__(self, n):
        self.wheels = [Wheel() for _ in range(n)]
    def count(self):
        return len(self.wheels)
print(Car(int(input())).count())    