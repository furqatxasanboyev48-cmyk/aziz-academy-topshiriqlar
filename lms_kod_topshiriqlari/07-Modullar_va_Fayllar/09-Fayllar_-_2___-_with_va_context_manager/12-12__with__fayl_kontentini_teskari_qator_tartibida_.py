n = int(input())
qatorlar = []
for _ in range(n):
    qatorlar.append(input())
with open("w12.txt", "w", encoding="utf-8") as f:
    for q in qatorlar:
        f.write(q + "\n")
with open("w12.txt", "r", encoding="utf-8") as f:
    hammasi = f.readlines()
for qator in reversed(hammasi):
    print(qator.rstrip("\n"))