class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
    def info(self):
        return f"{self.name}, {self.age}, {self.school}"
parts = input().split()
s = Student(parts[0], int(parts[1]), parts[2])
print(s.info())        