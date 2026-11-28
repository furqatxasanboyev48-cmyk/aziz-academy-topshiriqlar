class Time:
    def __init__(self, h, m):
        self.h = h 
        self.m = m 
    def __repr__(self):
        return f"Time(h={self.h}, m={self.m})"
try:
    h = int(input().strip())
    m = int(input().strip())
except ValueError:
    print("BAD")
else:
    if 0 <= h <= 23 and 0 <= m <= 59:
        print(repr(Time(h, m)))
    else:
        print("BAD")