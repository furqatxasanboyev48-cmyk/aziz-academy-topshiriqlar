class Player:
    def __init__(self, height):
        self.height = height
class Team:
    def __init__(self):
        self.players = []
    def add(self, p):
        self.players.append(p)
    def avg_height(self):
        return sum(p.height for p in self.players) // len(self.players)
hs = list(map(int, input().split()))
t = Team()
for h in hs:
    t.add(Player(h))
print(t.avg_height())
    