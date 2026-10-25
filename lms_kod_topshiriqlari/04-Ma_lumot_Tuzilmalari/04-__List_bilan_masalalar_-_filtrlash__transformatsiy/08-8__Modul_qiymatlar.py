n = int(input())
sonlar = list(map(int, input().split()))
modullar = []
for son in sonlar:
    modullar.append(abs(son))
print(modullar)