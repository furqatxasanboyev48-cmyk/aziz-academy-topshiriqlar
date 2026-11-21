class Counter:
    def __init__(self):
        self.count = 0 
    def increment(self):
        self.count += 1
c = Counter()
n = int(input())
for _ in range(n):
    c.increment()
print(c.count)