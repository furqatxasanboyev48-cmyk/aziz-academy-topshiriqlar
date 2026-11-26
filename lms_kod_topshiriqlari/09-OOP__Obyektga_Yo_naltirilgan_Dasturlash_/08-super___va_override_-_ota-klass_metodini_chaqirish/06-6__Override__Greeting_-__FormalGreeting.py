class Greeting:
    def __init__(self, name):
        self.name = name
    def hello(self):
        return f"Salom, {self.name}"
class FormalGreeting(Greeting):
    def hello(self):
        return f"Assalomu alaykum, hurmatli {self.name}"
print(FormalGreeting(input()).hello())