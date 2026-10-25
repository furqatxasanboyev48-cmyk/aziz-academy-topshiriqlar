n = int(input())
sonlar = input().split()
uzunliklar = []
for son in sonlar:
    uzunliklar.append(len(son))
print(uzunliklar)