import json
n = int(input())
kontaktlar = []
for _ in range(n):
    name, phone = input().split()
    kontaktlar.append((name, phone))
with open("pbook10.txt", "w", encoding="utf-8") as f:
    for name, phone in kontaktlar:
        f.write(name + "=" + phone + "\n")
kitob = {}
with open("pbook10.txt", "r", encoding="utf-8") as f:
    for qator in f:
        qator = qator.rstrip("\n")
        if qator:
            k, v = qator.split("=", 1)
            kitob[k] = v 
with open("pbook10.json", "w", encoding="utf-8") as f:
    json.dump(kitob, f, sort_keys=True, ensure_ascii=False)
with open("pbook10.json", "r", encoding="utf-8") as f:
    qayta = json.load(f)
print(len(qayta.keys()))