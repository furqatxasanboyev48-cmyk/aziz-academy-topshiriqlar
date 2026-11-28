class Time:
    def __init__(self, h, m):
        self.h = h 
        self.m = m 
    def __str__(self):
        return f"{self.h:02d}:{self.m:02d}"
try:
    h = int(input().strip())
    m = int(input().strip())
except ValueError:
    print("BAD")
else:
    if 0 <= h <= 23 and 0 <= m <= 59:
        print(Time(h, m))
    else:
        print("BAD")