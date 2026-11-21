class Person:
    def __init__(self, full_name):
        self.name = full_name.strip().title()
full_name = input()
if full_name.strip():
    print(Person(full_name).name)
else:
    print("BAD")
        