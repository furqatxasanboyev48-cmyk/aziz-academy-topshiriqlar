n = int(input())
qatorlar = []
for _ in range(n):
    qatorlar.append(input())
k = int(input())
with open("log13.txt", "w", encoding="utf-8") as f:
    for q in qatorlar:
        f.write(q + "\n")
with open("log13.txt", "r", encoding="utf-8") as f:
    hammasi = f.readlines()
for qator in hammasi[-k:]:
    print(qator.rstrip("\n"))