n = int(input())
sonlar = list(map(int, input().split()))
kvadratlar = []
for son in sonlar:
    kvadratlar.append(son * son)
print(kvadratlar)