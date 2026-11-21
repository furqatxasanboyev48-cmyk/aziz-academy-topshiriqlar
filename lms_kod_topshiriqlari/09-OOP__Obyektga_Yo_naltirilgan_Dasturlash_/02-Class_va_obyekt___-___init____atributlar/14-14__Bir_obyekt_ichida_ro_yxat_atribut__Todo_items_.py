class Todo:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
try:
    n = int(input().strip())
except ValueError:
    print("BAD")
else:
    if n < 0:
        print("BAD")
    else:
        todo = Todo()
        ok = True
        for _ in range(n + 1):
            item = input().strip()
            if not item:
                ok = False
                break
            todo.add(item)
        print(len(todo.items) if ok else "BAD")
                