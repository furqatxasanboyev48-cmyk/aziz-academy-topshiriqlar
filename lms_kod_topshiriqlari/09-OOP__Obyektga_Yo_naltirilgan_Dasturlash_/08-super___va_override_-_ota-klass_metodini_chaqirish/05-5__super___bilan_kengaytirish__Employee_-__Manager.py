class Employee:
    def __init__(self, base):
        self.base = base
    def salary(self):
        return self.base
class Manager(Employee):
    def __init__(self, base, bonus):
        super().__init__(base)
        self.bonus = bonus
    def salary(self):
        return super().salary() + self.bonus
b, bonus = map(int, input().split())   
print(Manager(b, bonus).salary())      