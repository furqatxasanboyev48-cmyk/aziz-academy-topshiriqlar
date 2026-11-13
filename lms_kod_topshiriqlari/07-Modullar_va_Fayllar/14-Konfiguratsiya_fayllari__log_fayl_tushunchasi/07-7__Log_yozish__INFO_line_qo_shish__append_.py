n = int(input())
xabarlar = []
for _ in range(n):
    xabarlar.append(input())
with open("log7.txt", "w", encoding="utf-8") as f:
    pass 
for xabar in xabarlar:
    with open("log7.txt", "a", encoding="utf-8") as f:
        f.write("INFO:" + xabar + "\n")
with open("log7.txt", "r", encoding="utf-8") as f:
    print(len(f.readlines()))    