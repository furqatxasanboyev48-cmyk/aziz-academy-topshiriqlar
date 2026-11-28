class SetLike:
    def __init__(self, items):
        self.values = set(items)
    def __len__(self):
        return len(self.values)
    def __eq__(self, other):
        return self.values == other.values
try:
    n = int(input().strip())
    if n < 0:
        raise ValueError
    items1 = [input().strip() for _ in range(n)]
    m = int(input().strip())    
    if m < 0:
         raise ValueError
    items2 = [input().strip() for _ in range(m)]
    s1, s2 = SetLike(items1), SetLike(items2)
    print(f"LEN1={len(s1)} LEN2={len(s2)}")
    print("EQ" if s1 == s2 else "NEQ")
except ValueError:
    print("BAD")
    