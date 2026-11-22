class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def is_adult(self):
        return self.age >= 18
name = input().strip()
try:
    age = int(input().strip())
except ValueError:
    print("BAD")
else:
    if name and 0 <= age <= 120:
        u = User(name, age)
        print("ADULT" if u.is_adult() else "MINOR")
    else:
        print("BAD")