matn = input()
unik = {h for h in matn.lower() if h in "aeiou"}
if unik:
    print(" ".join(sorted(unik)))
else:
    print("BO'SH")