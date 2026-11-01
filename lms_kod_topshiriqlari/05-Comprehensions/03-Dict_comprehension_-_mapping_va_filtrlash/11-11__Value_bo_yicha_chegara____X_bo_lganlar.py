n = int(input())
d = {}
for _ in range(n):
    kalit, qiymat = input().split()
    d[kalit] = int(qiymat)
x = int(input())
natija = {k: v for k, v in d.items() if v >= x}
print(natija)