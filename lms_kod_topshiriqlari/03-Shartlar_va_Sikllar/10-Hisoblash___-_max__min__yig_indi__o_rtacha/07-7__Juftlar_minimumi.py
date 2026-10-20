n = int(input())
parts = input().split()
found = False
m = 0
for p in parts:
    x = int(p)
    if x % 2 == 0:
        if not found or x < m:
            m = x
        found = True
if found:
        print(m)
else:
        print("No")