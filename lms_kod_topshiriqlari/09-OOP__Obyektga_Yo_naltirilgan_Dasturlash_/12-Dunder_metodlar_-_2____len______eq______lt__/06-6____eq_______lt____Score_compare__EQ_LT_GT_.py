class Score:
    def __init__(self, val):
        self.val = val 
    def __eq__(self, other):
        return self.val == other.val 
    def __lt__(self, other):
        return self.val < other.val 
try:
    a = int(input().strip())
    b = int(input().strip())
except ValueError:
    print("BAD")
else:
    s1, s2 = Score(a), Score(b)
    if s1 == s2:
        print("EQ")
    elif s1 < s2:
        print("LT")
    else:
        print("GT")