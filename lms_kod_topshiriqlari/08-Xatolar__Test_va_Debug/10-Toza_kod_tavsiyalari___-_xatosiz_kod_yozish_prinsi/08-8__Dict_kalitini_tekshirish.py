n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = v 
q = input().strip()
if q in d:
    print(d[q])
else:
    print("NOKEY")