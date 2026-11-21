class OrderLine:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty
    def total(self):
        return self.price * self.qty
class Invoice:
    def __init__(self,lines):
        self.lines = lines
    def subtotal(self):
        return sum(line.total() for line in self.lines)
try:
    n = int(input().strip())
    if n < 0:
        raise ValueError
    lines = []
    for _ in range(n):
        parts = input().split()
        if len(parts) != 3:
            raise ValueError
        name, price, qty = parts[0], int(parts[1]), int(parts[2])
        if price < 0 or qty < 0:
            raise ValueError
        lines.append(OrderLine(name, price, qty))
    print(f"SUBTOTAL={Invoice(lines).subtotal()}")    
except ValueError:
    print("BAD")