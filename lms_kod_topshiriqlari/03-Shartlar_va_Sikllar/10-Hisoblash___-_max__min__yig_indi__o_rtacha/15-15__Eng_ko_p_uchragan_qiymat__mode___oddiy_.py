n = int(input())
parts = input().split()
lst = []
for p in parts:
    lst.append(int(p))
best = lst[0]
bestc = 0
for x in lst:
    c = 0
    for y in lst:
        if y == x:
            c += 1
    if c > bestc or (c == bestc and x < best):
        best = x
        bestc = c
print(best)