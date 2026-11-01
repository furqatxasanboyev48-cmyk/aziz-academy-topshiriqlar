n = int(input())
d = {}
for _ in range(n):
    kalit, qiymat = input().split()
    d[kalit] = int(qiymat)
natija = {k: abs(v) for k, v in d.items() if abs(v) >= 5}
print(natija)