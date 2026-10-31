sozlar = input().split()
natija = [s for s in sozlar if len(s) >= 5]
if natija:
    print(" ".join(natija))
else:
    print("BO'SH")