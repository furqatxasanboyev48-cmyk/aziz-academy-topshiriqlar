class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def total_pay(self):
        return self.salary
class Developer(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def total_pay(self):
        return self.salary + self.bonus
try:
    kind = input().strip()
    name = input().strip()
    salary = int(input().strip())
    if kind == "EMP" and name and salary >= 0:
        print(Employee(name, salary).total_pay())
    elif kind == "DEV":
        bonus = int(input().strip())
        if name and salary >= 0 and bonus >= 0:
            print(Developer(name, salary, bonus).total_pay())
        else:
            print("BAD")
    else:
        print("BAD")
except ValueError:
    print("BAD")
    
        