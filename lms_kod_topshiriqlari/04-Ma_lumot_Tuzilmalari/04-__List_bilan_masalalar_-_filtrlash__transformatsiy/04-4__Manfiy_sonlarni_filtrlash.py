n = int(input())
sonlar = list(map(int, input().split()))
manfiylar = []
for son in sonlar:
    if son < 0:
        manfiylar.append(son)
print(manfiylar)