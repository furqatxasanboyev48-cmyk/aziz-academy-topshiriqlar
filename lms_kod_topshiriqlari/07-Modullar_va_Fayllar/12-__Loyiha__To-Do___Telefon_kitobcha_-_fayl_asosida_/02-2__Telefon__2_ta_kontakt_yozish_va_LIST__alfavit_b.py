name1, phone1 = input().split()
name2, phone2 = input().split()
with open("pbook2.txt", "w", encoding="utf-8") as f:
    f.write(name1 + "=" + phone1 + "\n")
    f.write(name2 + "=" + phone2 + "\n")
kitob = {}
with open("pbook2.txt", "r", encoding="utf-8") as f:
    for qator in f:
        qator = qator.rstrip("\n")
        if qator:
            k, v = qator.split("=", 1)
            kitob[k] = v 
for name in sorted(kitob):
    print(name, kitob[name])