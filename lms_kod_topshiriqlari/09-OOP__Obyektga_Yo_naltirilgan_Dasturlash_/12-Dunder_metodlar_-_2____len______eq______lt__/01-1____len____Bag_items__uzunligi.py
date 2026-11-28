class Bag:
    def __init__(self, items):
        self.items = items
    def __len__(self):
        return len(self.items)
try:
    n = int(input().strip())
    if n < 0:
        raise ValueError
    items = [input().strip() for _ in range(n)]    
    print(len(Bag(items)))
except ValueError:
    print("BAD")