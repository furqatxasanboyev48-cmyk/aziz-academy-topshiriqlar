sozlar = input().split()
unik = {s.lower() for s in sozlar}
print(" ".join(sorted(unik)))
