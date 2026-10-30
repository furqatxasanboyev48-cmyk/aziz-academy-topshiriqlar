sonlar = list(map(int, input().split()))
mean = sum(sonlar) / len(sonlar)
natija = []
for x in sonlar:
    natija.append("{:.2f}".format(x - mean))
print(" ".join(natija))