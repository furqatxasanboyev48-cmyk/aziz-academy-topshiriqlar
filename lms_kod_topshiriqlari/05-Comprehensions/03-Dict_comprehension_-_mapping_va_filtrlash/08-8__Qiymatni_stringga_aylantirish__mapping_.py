n = int(input())
d = {}
for _ in range(n):
    kalit, qiymat = input().split()
    d[kalit] = int(qiymat)
natija = {k: str(v) for k, v in d.items()}
print(natija)