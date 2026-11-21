class Telefon:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx
pul = int(input())
n = int(input())
telefonlar = []
for _ in range(n):
    qism = input().split()
    telefonlar.append(Telefon(qism[0], int(qism[1])))
topildi = False
for t in telefonlar:
    if t.narx <= pul:
        print(t.nom)
        topildi = True
if not topildi:
    print("Yo'q")

        