class Bag:
    def __init__(self, items):
        self._items = list(items)
    def add(self, item):
        self._items.append(item)
    def count(self):
        return len(self._items)
try:
    n = int(input().strip())
    if n < 0:
        raise ValueError
    items = []
    for _ in range(n):
        item = input().strip()
        if not item:
            raise ValueError
        items.append(item)
    bag = Bag(items)
    new_item = input().strip()
    if not new_item:
        raise ValueError
    bag.add(new_item)
    print(bag.count())
except ValueError:
    print("BAD")
    