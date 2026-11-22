class Timer:
    def __init__(self, seconds):
        self.seconds = seconds
    def tick(self):
        if self.seconds > 0:
            self.seconds -= 1
        return self.seconds
try:
    seconds = int(input().strip())
    k = int(input().strip())
except ValueError:
    print("BAD")
else:
    if seconds >= 0 and k >= 0:
        t = Timer(seconds)
        for _ in range(k):
            t.tick()
        print(t.seconds)
    else:
        print("BAD")
        
        