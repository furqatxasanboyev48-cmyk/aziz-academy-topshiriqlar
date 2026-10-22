parts = input().split()
n = int(parts[0])
m = int(parts[1])
x = int(input())
found = False
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i * j == x:
            found = True
if found:
    print("Yes")
else:
    print("No")