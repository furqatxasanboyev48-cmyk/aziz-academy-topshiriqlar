n = int(input())
d = {}
for _ in range(n):
    kalit, qiymat = input().split()
    d[kalit] = int(qiymat)
natija = {k: v for k, v in d.items() if v > 10}
print(natija)