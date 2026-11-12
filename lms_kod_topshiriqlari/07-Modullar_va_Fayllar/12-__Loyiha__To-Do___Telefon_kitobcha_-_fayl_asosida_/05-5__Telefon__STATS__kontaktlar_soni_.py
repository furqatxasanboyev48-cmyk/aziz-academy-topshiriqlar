n = int(input())
kontaktlar = []
for _ in range(n):
    name, phone = input().split()
    kontaktlar.append((name, phone))
with open("pbook5.txt", "w", encoding="utf-8") as f:
    for name, phone in kontaktlar:
        f.write(name + "=" + phone + "\n")
count = 0
with open("pbook5.txt", "r", encoding="utf-8") as f:
    for qator in f:
        if qator.strip():
            count += 1
print(count)