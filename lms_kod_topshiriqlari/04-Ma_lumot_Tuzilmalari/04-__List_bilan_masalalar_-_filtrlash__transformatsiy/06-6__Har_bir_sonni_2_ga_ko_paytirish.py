n = int(input())
sonlar = list(map(int, input().split()))
natija = []
for son in sonlar:
    natija.append(son * 2)
print(natija)