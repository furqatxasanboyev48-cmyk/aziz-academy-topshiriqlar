n = int(input())
sonlar = list(map(int, input().split()))
kattalar = []
for son in sonlar:
    if son > 10:
        kattalar.append(son)
print(kattalar)