n = int(input())
parts = input().split()
lst = []
for p in parts:
    lst.append(int(p))
k = int(input())
best = lst[0]
for x in lst:
    if abs(x - k) < abs(best - k):
        best = x
    elif abs(x - k) == abs(best - k) and x < best:
        best = x
print(best)
    