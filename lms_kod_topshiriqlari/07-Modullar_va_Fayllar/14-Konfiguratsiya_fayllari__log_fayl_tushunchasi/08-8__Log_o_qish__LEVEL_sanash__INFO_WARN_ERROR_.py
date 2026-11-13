n = int(input())
qatorlar = []
for _ in range(n):
    qatorlar.append(input())
with open("log8.txt", "w", encoding="utf-8") as f:
    for q in qatorlar:
        f.write(q + "\n")
sanash = {"INFO": 0, "WARN": 0, "ERROR": 0}
with open("log8.txt", "r", encoding="utf-8") as f:
    for qator in f:
        level = qator.split(":")[0].strip()
        if level in sanash:
            sanash[level] += 1
print("INFO", sanash["INFO"])
print("WARN", sanash["WARN"])
print("ERROR", sanash["ERROR"])