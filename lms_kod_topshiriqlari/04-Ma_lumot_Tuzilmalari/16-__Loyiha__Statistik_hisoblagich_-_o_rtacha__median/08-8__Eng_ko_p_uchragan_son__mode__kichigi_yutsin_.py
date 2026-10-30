sonlar = list(map(int, input().split()))
hisob = {}
for x in sonlar:
    hisob[x] = hisob.get(x, 0) + 1
moda = None
for x in sorted(hisob):
    if moda is None or hisob[x] > hisob[moda]:
        moda = x
print(moda)
