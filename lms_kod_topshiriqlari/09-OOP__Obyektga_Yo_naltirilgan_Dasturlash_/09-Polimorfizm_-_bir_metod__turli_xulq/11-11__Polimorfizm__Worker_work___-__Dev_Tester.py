class Worker:
    def __init__(self, name):
        self.name = name
    def work(self):
        return f"{self.name} works"
class Developer(Worker):
    def work(self):
        return f"{self.name} codes"
class Tester(Worker):
    def work(self):
        return f"{self.name} tests"
kind = input().strip()
name = input().strip()
classes = {"DEV": Developer, "TEST": Tester}
if kind in classes and name:
    print(classes[kind](name).work())
else:
    print("BAD")