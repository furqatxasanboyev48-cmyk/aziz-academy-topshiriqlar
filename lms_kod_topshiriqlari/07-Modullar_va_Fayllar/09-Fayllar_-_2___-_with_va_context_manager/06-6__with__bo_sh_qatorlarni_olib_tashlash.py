n = int(input())
qatorlar = []
for _ in range(n):
    qatorlar.append(input())
with open("w6.txt", "w", encoding="utf-8") as f:
    for q in qatorlar:
        f.write(q + "\n")
with open("w6.txt", "r", encoding="utf-8") as f:
    for qator in f:
        if qator.strip() != "":
            print(qator.rstrip("\n"))
        