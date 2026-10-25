n = int(input())
sonlar = list(map(int, input().split()))
musbatlar = []
for son in sonlar:
    if son > 0:
        musbatlar.append(son)
print(musbatlar)