class Mahsulot:
    chegirma = 10 
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx
nom = input().strip()
narx = int(input())
m = Mahsulot(nom, narx)
yangi_narx = m.narx - m.narx * Mahsulot.chegirma // 100
print(m.nom, yangi_narx)