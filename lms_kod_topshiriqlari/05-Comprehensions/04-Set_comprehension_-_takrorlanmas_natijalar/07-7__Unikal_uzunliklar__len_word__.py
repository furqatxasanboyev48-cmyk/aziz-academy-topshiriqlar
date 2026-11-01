sozlar = input().split()
unik = {len(s) for s in sozlar}
natija = [str(x) for x in sorted(unik)]
print(" ".join(natija))
