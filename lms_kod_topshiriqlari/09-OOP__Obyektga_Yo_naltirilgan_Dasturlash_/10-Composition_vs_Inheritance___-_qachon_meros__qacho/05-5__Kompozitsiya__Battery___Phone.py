class Battery:
    def __init__(self, level):
        self.level = level
class Phone:
    def __init__(self, level):
        self.battery = Battery(level)
    def status(self):
        return "OK" if self.battery.level > 20 else "Past"
print(Phone(int(input())).status())