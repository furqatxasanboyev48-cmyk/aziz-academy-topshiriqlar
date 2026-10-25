n = int(input())
sonlar = list(map(int, input().split()))
natija  = []
for son in sonlar:
    if son > 0:
        natija.append(son * 2)
print(natija)