n = int(input())
qatorlar = []
for _ in range(n):
    qatorlar.append(input())
with open("log9.txt", "w", encoding="utf-8") as f:
    for q in qatorlar:
        f.write(q + "\n")
with open("log9.txt", "r", encoding="utf-8") as f:
    for qator in f:
        qator = qator.rstrip("\n")
        if qator.startswith("ERROR:"):
            xabar = qator.split(":", 1)[1].strip()
            print(xabar)
        
    