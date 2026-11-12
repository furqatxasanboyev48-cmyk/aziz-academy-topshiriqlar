kontaktlar = []
for _ in range(3):
    name, phone = input().split()
    kontaktlar.append((name, phone))
delete_name = input().strip()
with open("pbook3.txt", "w", encoding="utf-8") as f:
    for name, phone in kontaktlar:
        f.write(name + "=" + phone + "\n")
kitob = {}
with open("pbook3.txt", "r", encoding="utf-8") as f:
    for qator in f:
        qator = qator.rstrip("\n")
        if qator:
            k, v = qator.split("=", 1)
            kitob[k] = v 
if delete_name in kitob:
    del kitob[delete_name]
for name in sorted(kitob):
    print(name, kitob[name])
    
    