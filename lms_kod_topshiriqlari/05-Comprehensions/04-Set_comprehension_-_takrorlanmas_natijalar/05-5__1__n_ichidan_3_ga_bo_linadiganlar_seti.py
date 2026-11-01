n = int(input())
unik = {x for x in range(1, n + 1) if x % 3 == 0}
if unik:
    natija = [str(x) for x in sorted(unik)]
    print(" ".join(natija))
else:
    print("BO'SH")