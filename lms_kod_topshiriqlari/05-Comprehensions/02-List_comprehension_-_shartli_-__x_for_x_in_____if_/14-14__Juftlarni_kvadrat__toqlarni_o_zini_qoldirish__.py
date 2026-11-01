sonlar = [int(x) for x in input().split()]
natija = [str(x * x) if x % 2 == 0 else str(x) for x in sonlar]
print(" ".join(natija))
