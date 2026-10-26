n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
for k, v in d.items():
    print(k, v)