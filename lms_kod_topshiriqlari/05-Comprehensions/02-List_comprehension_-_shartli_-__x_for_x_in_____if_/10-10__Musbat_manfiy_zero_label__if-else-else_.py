sonlar = [int(x) for x in input().split()]
natija = ["pos" if x > 0 else "neg" if x < 0 else "zero" for x in sonlar]
print(" ".join(natija))