n = int(input())
sonlar = list(map(int, input().split()))
toqlar = []
for son in sonlar:
    if son % 2 == 1:
        toqlar.append(son)
print(toqlar)