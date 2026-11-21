class Student:
    school = "PDP"
    def __init__(self, name):
        self.name = name
name = input().strip()
if name:
    s = Student(name)
    print(f"{s.name} @ {s.school}")
else:
    print("BAD")