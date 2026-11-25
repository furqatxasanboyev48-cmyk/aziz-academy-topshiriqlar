class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
    def pay(self):
        return self.salary
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def pay(self):
        return super().pay() + self.bonus
name = input().strip()
try:
    salary = int(input().strip())
    bonus = int(input().strip())
except ValueError:
    print("BAD")
else:
    if name and salary >= 0 and bonus >= 0:
        print(Manager(name, salary, bonus).pay())
    else:
        print("BAD")
    