n = int(input())
natija = {}
korilgan = set()
for _ in range(n):
    kalit, qiymat = input().split()
    qiymat = int(qiymat)
    if qiymat not in korilgan:
        korilgan.add(qiymat)
        natija[kalit] = qiymat
print(natija)