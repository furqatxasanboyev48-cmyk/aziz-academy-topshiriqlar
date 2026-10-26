n = int(input())
d = {}
for _ in range(n):
    k , v = input().split()
    d[k] = int(v)
yangi = {}
for k, v in d.items():
    yangi[k] = v * 2
print(yangi)