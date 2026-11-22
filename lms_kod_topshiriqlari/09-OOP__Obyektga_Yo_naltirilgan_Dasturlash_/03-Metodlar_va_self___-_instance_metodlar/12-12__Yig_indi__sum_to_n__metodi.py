class RangeSum:
    def __init__(self, base):
        self.base = base
    def sum_to(self, n):
        return self.base + sum(range(1, n + 1))
try:
    base = int(input().strip())
    n = int(input().strip())
except ValueError:
    print("BAD")
else:
    if n >= 0:
        print(RangeSum(base).sum_to(n))
    else:
         print("BAD")  