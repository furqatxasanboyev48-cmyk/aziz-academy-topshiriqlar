class Room:
    def __init__(self, area):
        self.area = area
class House:
    def __init__(self):
        self.rooms = []
    def add(self, r):
        self.rooms.append(r)
    def total_area(self):
        return sum(r.area for r in self.rooms)
areas = list(map(int, input().split()))       
h = House()
for a in areas:
    h.add(Room(a))
print(h.total_area())