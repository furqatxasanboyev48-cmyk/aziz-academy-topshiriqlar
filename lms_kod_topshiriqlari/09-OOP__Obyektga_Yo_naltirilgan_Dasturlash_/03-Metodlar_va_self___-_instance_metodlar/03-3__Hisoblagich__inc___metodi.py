class Counter:
    def __init__(self, start):
        self.value = start 
    def inc(self):
        self.value += 1
try:
    start = int(input().strip())
    n = int(input().strip())
except ValueError:
    print("BAD")
else:
    if n >= 0:
        c = Counter(start)
        for _ in range(n):
            c.inc()
        print(c.value)
    else:
        print("BAD")
    