class Notes:
    def __init__(self):
        self._notes = []
    def add(self, note):
        self._notes.append(note)
    def all(self):
        return self._notes.copy()
try:
    n = int(input().strip())
    if n < 0:
        raise ValueError
    notes = Notes()
    for _ in range(n):
        note = input().strip()
        if not note:
            raise ValueError
        notes.add(note)
    items = notes.all()
    print("|".join(items) if items else "NONE")
except ValueError:
    print("BAD")