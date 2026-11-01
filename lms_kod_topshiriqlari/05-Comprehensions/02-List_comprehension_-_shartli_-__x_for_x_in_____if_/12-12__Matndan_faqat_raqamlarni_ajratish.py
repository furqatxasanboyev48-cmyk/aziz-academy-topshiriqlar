matn = input()
raqamlar = [h for h in matn if h.isdigit()]
if raqamlar:
    print("".join(raqamlar))
else:
    print("BO'SH")