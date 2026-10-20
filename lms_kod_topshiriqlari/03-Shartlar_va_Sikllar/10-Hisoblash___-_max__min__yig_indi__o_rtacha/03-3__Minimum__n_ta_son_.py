n = int(input())
parts = input().split()
m = int(parts[0])
for p in parts:
    x = int(p)
    if x < m:
        m = x
print(m)