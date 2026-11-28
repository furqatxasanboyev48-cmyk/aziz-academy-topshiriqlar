class Username:
    def __init__(self, name):
        self.name = name 
    def __eq__(self, other):
        return self.name.lower() == other.name.lower()
u1 = input().strip()
u2 = input().strip()
if u1 and u2:
    print("YES" if Username(u1) == Username(u2) else "NO")
else:
    print("BAD")