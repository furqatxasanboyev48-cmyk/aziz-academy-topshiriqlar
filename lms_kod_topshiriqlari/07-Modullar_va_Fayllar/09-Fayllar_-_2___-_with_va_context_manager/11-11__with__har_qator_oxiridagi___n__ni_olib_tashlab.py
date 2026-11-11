n = int(input())
qatorlar = []
for _ in range(n):
    qatorlar.append(input())
with open("w11.txt", "w", encoding="utf-8") as f:
    for q in qatorlar:
        f.write(q + "\n")
with open("w11.txt", "r", encoding="utf-8") as f:
    for qator in f:
        print(qator.rstrip("\n"))