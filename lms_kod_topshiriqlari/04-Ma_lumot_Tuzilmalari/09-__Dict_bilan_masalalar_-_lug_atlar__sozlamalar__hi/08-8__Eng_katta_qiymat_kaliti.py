n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
eng = None
mx = None
for k in d:
    if mx is None or d[k] > mx:
        mx = d[k]
        eng = k
print(eng)