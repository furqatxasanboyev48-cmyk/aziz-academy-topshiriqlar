n = int(input())
qatorlar = []
for _ in range(n):
    qatorlar.append(input())
with open("w8.txt", "w", encoding="utf-8") as f:
    for q in qatorlar:
        f.write(q + "\n")
with open("w8.txt", "r", encoding="utf-8") as f:
    k = 1
    for qator in f:
        print(f"{k}) {qator.rstrip(chr(10))}")
        k += 1
        