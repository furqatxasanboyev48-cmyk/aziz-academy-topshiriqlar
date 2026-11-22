class Todo:
    def __init__(self, items):
        self.items = items
    def add(self,item):
        self.items.append(item)
try:
    n = int(input().strip())
    if n < 0:
        raise ValueError
    items = []
    for _ in range(n):
        item = input().strip()
        if not item:
            raise ValueError
        items.append(item)
    todo = Todo(items)
    new_item = input().strip()
    if not new_item:
        raise ValueError
    todo.add(new_item)
    print(todo.items[-1])
except ValueError:
    print("BAD")
        
        
            
    
    
        