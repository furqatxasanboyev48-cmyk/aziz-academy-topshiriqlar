n = int(input())
qatorlar = []
for _ in range(n):
    qatorlar.append(input())
with open("enc8.txt", "w", encoding="utf-8") as f:
    for q in qatorlar:
        f.write(q + "\n")
with open("enc8.txt", "r", encoding="utf-8") as f:
    print(len(f.readlines()))
    