class Version:
    def __init__(self, x, y, z):
        self.parts = (x, y, z)
    def __eq__(self, other):
        return self.parts == other.parts
    def __lt__(self, other):
        return self.parts < other.parts
def parse(s):
    parts = s.strip().split(".")
    if len(parts) != 3:
        return None
    nums = []
    for p in parts:
        v = int(p)
        if v < 0:
            return None 
        nums.append(v)
    return Version(*nums)
try:
    v1 = parse(input())
    v2 = parse(input())
except ValueError:
    print("BAD")
else:
    if v1 is None or v2 is None:
        print("BAD")
    elif v1 == v2:
        print("EQ")
    elif v1 < v2:
        print("LT")
    else:
        print("GT")