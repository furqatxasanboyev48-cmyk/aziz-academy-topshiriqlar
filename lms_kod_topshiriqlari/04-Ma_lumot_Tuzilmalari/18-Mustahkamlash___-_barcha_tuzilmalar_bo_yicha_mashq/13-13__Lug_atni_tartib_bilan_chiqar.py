n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = v
for k in sorted(d):
    print(k + "=" + d[k])
    