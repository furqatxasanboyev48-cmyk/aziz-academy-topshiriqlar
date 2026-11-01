sozlar = input().split()
juftlar = {(s.lower(), len(s)) for s in sozlar}
print(len(juftlar))
for soz, uzunlik in sorted(juftlar):
    print(f"{soz}:{uzunlik}")