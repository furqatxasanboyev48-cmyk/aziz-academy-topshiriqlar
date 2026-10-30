sonlar = list(map(int, input().split()))
juftlar = 0
toqlar = 0
for x in sonlar:
    if x % 2 == 0:
        juftlar += 1
    else:
        toqlar += 1
print(juftlar)
print(toqlar)