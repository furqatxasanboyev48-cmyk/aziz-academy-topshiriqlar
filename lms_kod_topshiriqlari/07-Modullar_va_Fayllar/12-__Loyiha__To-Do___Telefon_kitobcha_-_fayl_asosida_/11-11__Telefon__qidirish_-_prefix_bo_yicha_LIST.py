n = int(input())
kontaktlar = []
for _ in range(n):
    name, phone = input().split()
    kontaktlar.append((name, phone))
prefix = input().strip()
with open("pbook11.txt", "w", encoding="utf-8") as f:
    for name, phone in kontaktlar:
        f.write(name + "=" + phone + "\n")
kitob = {}
with open("pbook11.txt", "r", encoding="utf-8") as f:
    for qator in f:
        qator = qator.rstrip("\n")
        if qator:
            k, v = qator.split("=", 1)
            kitob[k] = v 
for name in sorted(kitob):
    if name.startswith(prefix):
        print(name, kitob[name])
    
        