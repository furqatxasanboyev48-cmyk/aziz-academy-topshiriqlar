class Cart:
    def __init__(self):
        self.items = {}
    def add(self, name, price, qty):
        if not name or price < 0 or qty <= 0:
            return False
        if name in self.items:
            if self.items[name][0] != price: 
                return False
            self.items[name][1] += qty
        else:
            self.items[name] = [price, qty]
        return True
    def total(self):
        return sum(p * q for p, q in self.items.values())
try:
    q = int(input().strip())
    if q < 0:
        raise ValueError
    cart = Cart()
    out = []
    for _ in range(q):
        parts = input().split()
        if len(parts) == 4 and parts[0] == "ADD":
            if not cart.add(parts[1], int(parts[2]), int(parts[3])):
                raise ValueError
        elif len(parts) == 1 and parts[0] == "TOTAL":
            out.append(str(cart.total()))
        else:
            raise ValueError
    if out:
        print("\n".join(out))
except ValueError:
   print("BAD")