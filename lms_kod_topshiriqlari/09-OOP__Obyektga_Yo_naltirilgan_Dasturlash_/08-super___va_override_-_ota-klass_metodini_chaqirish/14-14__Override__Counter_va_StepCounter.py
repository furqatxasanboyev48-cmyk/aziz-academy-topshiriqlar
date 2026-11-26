class Counter:
    def __init__(self):
        self.value = 0 
    def inc(self):
        self.value += 1 
class StepCounter(Counter):
    def __init__(self, step):
        super().__init__()
        self.step = step 
    def inc(self):
        self.value += self.step 
step, times = map(int, input().split())
c = StepCounter(step)
for _ in range(times):
    c.inc()
print(c.value)