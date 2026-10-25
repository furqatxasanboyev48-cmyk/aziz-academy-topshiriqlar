n = int(input())
sonlar = list(map(int, input().split()))
natija = []
for son in sonlar:
    if son % 2 == 1:
        natija.append(son * son)
print(natija)