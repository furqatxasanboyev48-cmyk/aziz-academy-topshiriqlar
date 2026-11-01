n = int(input())
natija = [str(x) for x in range(1, n + 1) if x % 3 == 0]
if natija:
    print(" ".join(natija))
else:
    print("BO'SH")

