n = int(input())
qatorlar = []
for _ in range(n):
    qatorlar.append(input())
with open("w13.txt", "w", encoding="utf-8") as f:
    for q in qatorlar:
        f.write(q + "\n")
jami = 0
with open("w13.txt", "r", encoding="utf-8") as f:
    for qator in f:
        qator = qator.strip()
        if qator:
            key, value = qator.split("=", 1)
            jami += int(value)
print(jami)