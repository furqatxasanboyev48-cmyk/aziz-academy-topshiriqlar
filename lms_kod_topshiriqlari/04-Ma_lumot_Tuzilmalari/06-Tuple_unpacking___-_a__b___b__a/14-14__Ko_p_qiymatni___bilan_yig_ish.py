n = int(input())
sonlar = list(map(int, input().split()))
birinchi, *qolganlar = sonlar
print(birinchi)
print(qolganlar)