n = int(input())
qatorlar = []
for _ in range(n):
    qatorlar.append(input())
with open("w9.txt", "w", encoding="utf-8") as f:
    for q in qatorlar:
        f.write(q + "\n")
with open("w9.txt", "r", encoding="utf-8") as f:
    max_len = 0
    for qator in f:
        qator = qator.rstrip("\n")
        if len(qator) > max_len:
            max_len = len(qator)
print(max_len)