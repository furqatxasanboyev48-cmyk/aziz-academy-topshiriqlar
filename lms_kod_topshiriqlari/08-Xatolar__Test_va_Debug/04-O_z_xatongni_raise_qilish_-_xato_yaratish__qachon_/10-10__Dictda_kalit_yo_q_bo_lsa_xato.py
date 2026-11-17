n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = v 
q = input().strip()
try:
    if q not in d:
        raise KeyError(q)
except KeyError:
    print("NOKEY")
else:
    print("FOUND")