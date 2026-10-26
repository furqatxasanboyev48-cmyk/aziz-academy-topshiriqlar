n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
eng = None
mn = None
for k in d:
    if mn is None or d[k] < mn:
        mn = d[k]
        eng = k
print(eng)