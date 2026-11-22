class Score:
    def __init__(self, start):
        self.value = start
    def add(self, points):
        self.value += points
        return 0 <= self.value <= 100
    def grade(self):
        if self.value >= 90:
            return "A"
        if self.value >= 70:
            return "B"
        if self.value >= 50:
            return "C"
        return "D"
try:
    start = int(input().strip())
    points = int(input().strip())
except ValueError:
    print("BAD")
else:
    if 0 <= start <= 100:
        s = Score(start)
        print(s.grade() if s.add(points) else "BAD")
    else:
        print("BAD")
        
        
        
        