n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
for v in d.values():
    if v > 50:
        print(v)
        