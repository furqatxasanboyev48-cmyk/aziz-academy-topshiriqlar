n1 = int(input())
a_kontaktlar = []
for _ in range(n1):
    name, phone = input().split()
    a_kontaktlar.append((name, phone))
n2 = int(input())
b_kontaktlar = []
for _ in range(n2):
    name, phone = input().split()
    b_kontaktlar.append((name, phone))
with open("pbook14_a.txt", "w", encoding="utf-8") as f:
    for name, phone in a_kontaktlar:
        f.write(name + "=" + phone + "\n")
with open("pbook14_b.txt", "w", encoding="utf-8") as f:
    for name, phone in b_kontaktlar:
        f.write(name + "=" + phone + "\n")
kitob = {}
for fayl in ["pbook14_a.txt", "pbook14_b.txt"]:
    with open(fayl, "r", encoding="utf-8") as f:
        for qator in f:
            qator = qator.rstrip("\n")
            if qator:
                k, v = qator.split("=", 1)
                kitob[k] = v 
for name in sorted(kitob):
    print(name, kitob[name])
    