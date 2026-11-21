class Stack:
    def __init__(self):
        self._items = []
    def push(self, x):
        self._items.append(x)
    def pop(self):
        return self._items.pop()
    def size(self):
        return len(self._items)
nums = list(map(int, input().split()))
s = Stack()
for x in nums:
    s.push(x)
top = s.pop()
print(top, s.size())
        