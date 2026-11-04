counter = 0
logs = []
def add(msg):
    global counter
    logs.append(msg)
    counter += 1
def stats():
    return f"count={counter}, logs={len(logs)}"
n = int(input())
for i in range(n):
    add(input())
print(stats())