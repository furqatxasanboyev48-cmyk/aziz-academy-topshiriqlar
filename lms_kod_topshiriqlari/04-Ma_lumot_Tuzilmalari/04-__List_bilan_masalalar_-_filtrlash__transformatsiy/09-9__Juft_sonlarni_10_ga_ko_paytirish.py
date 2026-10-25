n = int(input())
sonlar = list(map(int, input().split()))
natija = []
for son in sonlar:
    if son % 2 == 0:
        natija.append(son * 10)
print(natija)