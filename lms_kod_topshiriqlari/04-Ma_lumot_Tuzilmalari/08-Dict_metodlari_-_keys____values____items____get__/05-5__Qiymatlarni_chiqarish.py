n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
for qiymat in d.values():
    print(qiymat)