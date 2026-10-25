n = int(input())
sozlar = input().split()
natija = []
for soz in sozlar:
    if len(soz) >= n:
        natija.append(soz)
print(natija)