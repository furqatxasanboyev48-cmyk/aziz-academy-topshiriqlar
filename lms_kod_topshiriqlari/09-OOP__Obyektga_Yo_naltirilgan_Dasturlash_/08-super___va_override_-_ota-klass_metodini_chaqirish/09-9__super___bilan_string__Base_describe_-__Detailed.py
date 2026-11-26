class Base:
    def describe(self):
        return "Obyekt "
class Detailed(Base):
    def __init__(self, name):
        self.name = name
    def describe(self):
        return super().describe() + f"nomi {self.name}"
print(Detailed(input()).describe())    