class Score:
    def __init__(self, val):
        self.val = val 
    def __lt__(self, other):
        return self.val < other.val 
try:
    a = int(input().strip())
    b = int(input().strip())
except ValueError:
    print("BAD")
else:
    print("LT" if Score(a) < Score(b) else "GE")