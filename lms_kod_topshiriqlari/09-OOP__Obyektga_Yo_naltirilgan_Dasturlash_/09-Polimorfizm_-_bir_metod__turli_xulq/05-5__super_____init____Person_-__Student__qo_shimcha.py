class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
    def info(self):
        return f"{self.name} grade={self.grade}"
name = input().strip()
try:
    grade = int(input().strip())
except ValueError:
    print("BAD")
else:
    if name and 1 <= grade <= 11:
        print(Student(name, grade).info())
    else:
        print("BAD")