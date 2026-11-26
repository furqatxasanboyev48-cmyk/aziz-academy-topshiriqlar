class BaseList:
    def __init__(self, items):
        self._items = items
class SumList(BaseList):
    def total(self):
        return sum(self._items)
try:
    n = int(input().strip())
    if n < 0:
        raise ValueError
    items = [int(input().strip()) for _ in range(n)]
    print(SumList(items).total())
except ValueError:
    print("BAD")