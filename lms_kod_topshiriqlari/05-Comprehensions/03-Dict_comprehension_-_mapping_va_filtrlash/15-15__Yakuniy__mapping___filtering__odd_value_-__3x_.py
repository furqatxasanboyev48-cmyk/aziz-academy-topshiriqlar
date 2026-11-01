n = int(input())
d = {}
for _ in range(n):
    kalit, qiymat = input().split()
    d[kalit] = int(qiymat)
natija = {k: v * 3 if v % 2 != 0 else v * 2 for k, v in d.items() if abs(v) >= 2}
print(natija)