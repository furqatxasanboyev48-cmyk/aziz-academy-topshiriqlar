sozlar = input().split()
unik = {s.lower() for s in sozlar if s.lower() == s.lower()[::-1]}
if unik:
    print(" ".join(sorted(unik)))
else:
    print("BO'SH")