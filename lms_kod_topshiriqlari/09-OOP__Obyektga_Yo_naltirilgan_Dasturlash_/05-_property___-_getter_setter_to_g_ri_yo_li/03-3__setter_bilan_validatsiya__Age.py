class Person:
    def __init__(self):
        self._age = 0
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, v):
        self._age = v if v >= 0 else 0
p = Person()
p.age = int(input())
print(p.age)