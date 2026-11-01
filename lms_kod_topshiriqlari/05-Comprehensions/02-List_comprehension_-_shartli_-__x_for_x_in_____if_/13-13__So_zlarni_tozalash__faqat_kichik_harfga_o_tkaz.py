sozlar = input().split()
natija = [s.lower() for s in sozlar if s.lower().startswith("a")]
if natija:
    print(" ".join(natija))
else:
    print("BO'SH")