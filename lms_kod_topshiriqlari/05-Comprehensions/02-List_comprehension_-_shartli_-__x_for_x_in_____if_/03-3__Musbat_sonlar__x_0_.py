sonlar = [int(x) for x in input().split()]
natija = [str(x) for x in sonlar if x > 0]
if natija:
    print(" ".join(natija))
else:
    print("BO'SH")