sonlar = list(map(int, input().split()))
hisob = {}
for x in sonlar:
    hisob[x] = hisob.get(x, 0) + 1
yagona = []
for x in sorted(hisob):
    if hisob[x] == 1:
        yagona.append(x)
if yagona:
    print(" ".join(str(x) for x in yagona))
else:
    print("EMPTY")