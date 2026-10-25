n = int(input())
sonlar = list(map(int, input().split()))
natija = []
for son in sonlar:
    if 0 < son < 100:
        natija.append(son)
print(natija)