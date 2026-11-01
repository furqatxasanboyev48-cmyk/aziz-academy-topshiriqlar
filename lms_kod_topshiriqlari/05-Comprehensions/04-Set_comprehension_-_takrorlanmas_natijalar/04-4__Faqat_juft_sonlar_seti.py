sonlar = [int(x) for x in input().split()]
unik = {x for x in sonlar if x % 2 == 0}
if unik:
    natija = [str(x) for x in sorted(unik)]
    print(" ".join(natija))
else:
    print("BO'SH")
    