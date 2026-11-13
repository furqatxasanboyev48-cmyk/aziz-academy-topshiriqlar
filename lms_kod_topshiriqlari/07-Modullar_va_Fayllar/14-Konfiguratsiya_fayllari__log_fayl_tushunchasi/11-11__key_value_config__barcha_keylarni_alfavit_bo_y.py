n = int(input())
qatorlar = []
for _ in range(n):
    qatorlar.append(input())
with open("cfg11.txt", "w", encoding="utf-8") as f:
    for q in qatorlar:
        f.write(q + "\n")
cfg = {}
with open("cfg11.txt", "r", encoding="utf-8") as f:
    for qator in f:
        qator = qator.rstrip("\n")
        if qator:
            k, v = qator.split("=", 1)
            cfg[k] = v 
for key in sorted(cfg):
    print(key)