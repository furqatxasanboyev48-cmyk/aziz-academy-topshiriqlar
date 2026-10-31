tokenlar = input().split()
natija = [t for t in tokenlar if t.isalpha()]
if natija:
    print(" ".join(natija))
else:
    print("BO'SH")