class Inventory:
    def __init__(self, items):
        self.items = items
    def remove(self, target):
        if target in self.items:
            self.items.remove(target)
            return True
        return False
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
    target = input().strip()
    if not target:
        raise  ValueError
    inv = Inventory(items)
    print("REMOVED" if inv.remove(target) else "NOTFOUND")
except ValueError:
    print("BAD")
                