class CPU:
    def __init__(self, ghz):
        self.ghz = ghz
class Computer:
    def __init__(self, ghz):
        self.cpu = CPU(ghz)
    def info(self):
        return f"CPU: {self.cpu.ghz} GHz"
print(Computer(int(input())).info())    