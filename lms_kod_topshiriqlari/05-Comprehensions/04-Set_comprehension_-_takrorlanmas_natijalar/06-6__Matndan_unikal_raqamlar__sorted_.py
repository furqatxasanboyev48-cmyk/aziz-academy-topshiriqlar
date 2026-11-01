matn = input()
unik = {h for h in matn if h.isdigit()}
if unik:
    print(" ".join(sorted(unik)))
else:
    print("BO'SH")