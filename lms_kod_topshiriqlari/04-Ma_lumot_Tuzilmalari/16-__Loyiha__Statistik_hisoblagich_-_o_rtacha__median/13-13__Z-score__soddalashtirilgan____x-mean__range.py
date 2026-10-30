sonlar = list(map(int, input().split()))
mean = sum(sonlar) / len(sonlar)
oraliq = max(sonlar) - min(sonlar)
natija = []
for x in sonlar:
    if oraliq == 0:
        natija.append("0.00")
    else:
        natija.append("{:.2f}".format((x - mean) / oraliq))
print(" ".join(natija))