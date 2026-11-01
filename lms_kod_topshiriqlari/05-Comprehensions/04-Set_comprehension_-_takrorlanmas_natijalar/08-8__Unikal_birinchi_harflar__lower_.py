sozlar = input().split()
unik = {s[0].lower() for s in sozlar}
print(" ".join(sorted(unik)))