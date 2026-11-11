n = int(input())
balllar = []
for _ in range(n):
    balllar.append(input())
with open("w15.txt", "w", encoding="utf-8") as f:
    for b in balllar:
        f.write(b + "\n")
sonlar = []
with open("w15.txt", "r", encoding="utf-8") as f:
    for qator in f:
        qator = qator.strip()
        if qator:
            sonlar.append(int(qator))
print(len(sonlar))
print(sum(sonlar))
print(f"{sum(sonlar) / len(sonlar):.2f}")
        
