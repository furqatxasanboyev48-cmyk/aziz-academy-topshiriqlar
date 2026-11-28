class Task:
    def __init__(self, priority):
        self.priority = priority
    def __lt__(self, other):
        return self.priority < other.priority
try:
    p1 = int(input().strip())
    p2 = int(input().strip())
except ValueError:
    print("BAD")
else:
    if 1 <= p1 <= 5 and 1 <= p2 <= 5:
        print("LT" if Task(p1) < Task(p2) else "GE")
    else:
        print("BAD")