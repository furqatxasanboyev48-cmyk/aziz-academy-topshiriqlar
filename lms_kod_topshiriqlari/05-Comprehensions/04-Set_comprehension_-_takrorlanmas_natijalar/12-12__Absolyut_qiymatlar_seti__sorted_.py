sonlar = [int(x) for x in input().split()]
unik = {abs(x) for x in sonlar}
natija = [str(x) for x in sorted(unik)]
print(" ".join(natija))