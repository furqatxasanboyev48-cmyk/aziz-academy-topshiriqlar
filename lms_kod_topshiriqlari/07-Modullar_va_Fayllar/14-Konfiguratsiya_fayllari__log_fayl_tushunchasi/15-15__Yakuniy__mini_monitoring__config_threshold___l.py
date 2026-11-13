threshold = int(input())
n = int(input())
qatorlar = []
for _ in range(n):
    qatorlar.append(input())
with open("cfg15.txt", "w", encoding="utf-8") as f:
    f.write("threshold=" + str(threshold) + "\n")
with open("log15.txt", "w", encoding="utf-8") as f:
    for q in qatorlar:
        f.write(q + "\n")
error_soni = 0
with open("log15.txt", "r", encoding="utf-8") as f:
    for qator in f:
        if qator.startswith("ERROR"):
            error_soni += 1
if error_soni > threshold:
    print("ALERT")
else:
    print("OK")