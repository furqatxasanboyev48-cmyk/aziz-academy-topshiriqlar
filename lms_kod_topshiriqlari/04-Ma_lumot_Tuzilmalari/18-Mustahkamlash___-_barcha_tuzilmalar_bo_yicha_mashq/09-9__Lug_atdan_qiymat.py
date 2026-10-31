n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = v
q = input()
print(d[q])