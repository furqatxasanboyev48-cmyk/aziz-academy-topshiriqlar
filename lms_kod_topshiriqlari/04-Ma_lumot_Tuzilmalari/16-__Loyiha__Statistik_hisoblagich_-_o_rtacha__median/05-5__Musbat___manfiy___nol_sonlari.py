sonlar = list(map(int, input().split()))
musbat = 0
manfiy = 0
nol = 0
for x in sonlar:
    if x > 0:
        musbat += 1
    elif x < 0:
        manfiy += 1
    else:
        nol += 1
print(musbat)
print(manfiy)
print(nol)