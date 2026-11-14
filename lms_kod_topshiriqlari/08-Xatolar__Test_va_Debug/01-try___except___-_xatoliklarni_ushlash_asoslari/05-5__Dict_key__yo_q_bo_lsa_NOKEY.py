n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
q = input().strip()
try:
    print(d[q])
except KeyError:
    print("NOKEY")
