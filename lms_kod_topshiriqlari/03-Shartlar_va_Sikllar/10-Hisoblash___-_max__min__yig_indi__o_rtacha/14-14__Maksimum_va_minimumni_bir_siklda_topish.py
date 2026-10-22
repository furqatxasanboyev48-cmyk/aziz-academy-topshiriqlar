n = int(input())
parts = input().split()
mx = int(parts[0])
mn = int(parts[0])
for p in parts:
    x = int(p)
    if x > mx:
        mx = x
    if x < mn:
        mn = x
print(mx, mn)