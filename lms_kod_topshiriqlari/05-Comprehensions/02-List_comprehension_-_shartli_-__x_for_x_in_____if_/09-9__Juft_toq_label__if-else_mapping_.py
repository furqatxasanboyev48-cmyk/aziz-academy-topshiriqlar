sonlar = [int(x) for x in input().split()]
natija = ["even" if  x % 2 == 0 else "odd" for x in sonlar]
print(" ".join(natija))