class Queue:
    def __init__(self, items):
        self.items = list(items)
    def __len__(self):
        return len(self.items)
    def enqueue(self, x):
        self.items.append(x)
    def dequeue(self):
        if not self.items:
            return False
        self.items.pop(0)
        return True
try:
    n = int(input().strip())
    if n < 0:
        raise ValueError
    items = [input().strip() for _ in range(n)]   
    q = Queue(items)
    op = input().strip()
    if op == "ENQ":
        x = input().strip()
        if not x:
            raise ValueError
        q.enqueue(x)
    elif op == "DEQ":
        if not q.dequeue():
            raise ValueError
    else:
            raise ValueError
    print(len(q))  
except ValueError:
    print("BAD")