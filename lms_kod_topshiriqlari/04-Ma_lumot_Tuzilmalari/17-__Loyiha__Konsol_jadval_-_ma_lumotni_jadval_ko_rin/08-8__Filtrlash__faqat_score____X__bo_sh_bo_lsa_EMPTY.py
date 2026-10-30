n = int(input())
rows = []
for _ in range(n):
    name, score = input().split()
    rows.append((name, int(score)))
x = int(input())
tanlangan = []
for name, score in rows:
    if score >= x:
        tanlangan.append((name, score))
if tanlangan:
    for name, score in tanlangan:
        print("{}={}".format(name, score))
else:
    print("EMPTY")
        