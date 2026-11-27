class Order:
    def __init__(self, lines):
        self.lines = lines
    def subtotal(self):
        return sum(price * qty for price, qty in self.lines)
class DiscountOrder(Order):
    def __init__(self, lines, percent):
        super().__init__(lines)
        self.percent = percent
    def subtotal(self):
        s = super().subtotal()
        return int(s * (100 - self.percent) / 100)
try:
    kind = input().strip()
    if kind not in ("BASE", "DISC"):
        raise ValueError
    n = int(input().strip())
    if n < 0:
        raise ValueError
    lines = []
    for _ in range(n):
        parts = input().split()
        if len(parts) != 2:
            raise ValueError
        price, qty = int(parts[0]), int(parts[1])
        if price < 0 or qty < 0:
            raise ValueError
        lines.append((price, qty))    
    if kind == "BASE":
        print(Order(lines).subtotal())
    else:
        percent = int(input().strip())
        if not 0 <= percent <= 100:
            raise ValueError
        print(DiscountOrder(lines, percent).subtotal())    
except ValueError:
        print("BAD")