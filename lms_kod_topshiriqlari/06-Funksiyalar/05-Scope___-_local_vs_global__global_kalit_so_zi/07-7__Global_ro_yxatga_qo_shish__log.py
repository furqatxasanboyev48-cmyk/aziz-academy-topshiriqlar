logs = []
def add_log(msg):
    logs.append(msg)
n = int(input())
for i in range(n):
    add_log(input())
print(len(logs))
for msg in logs:
     print(msg)