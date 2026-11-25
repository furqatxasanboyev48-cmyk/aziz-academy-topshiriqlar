class Widget:
    count = 0
    def __init__(self):
        Widget.count += 1 
    @classmethod
    def total(cls):
        return cls.count
n = int(input())
for _ in range(n):
    Widget()
print(Widget.total())
    