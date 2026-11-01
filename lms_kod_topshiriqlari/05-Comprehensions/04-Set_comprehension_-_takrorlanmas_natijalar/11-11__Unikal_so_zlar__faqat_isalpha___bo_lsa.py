tokenlar = input().split()
unik = {t.lower() for t in tokenlar if t. isalpha()}
if unik:
    print(" ".join(sorted(unik)))
else:
    print("BO'SH")
   