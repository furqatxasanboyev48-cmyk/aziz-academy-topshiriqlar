import csv
n = int(input())
rows = []
for _ in range(n):
    name, score = input().split()
    rows.append([name, score])
with open("c12.csv", "w", newline="") as f:
    yozgich = csv.writer(f)
    for row in rows:
        yozgich.writerow(row)
yozuvlar = []
with open("c12.csv", "r", newline="") as f:
    for row in csv.reader(f):
        yozuvlar.append((row[0], int(row[1])))
yozuvlar.sort(key=lambda y: (-y[1], y[0]))
for name, score in yozuvlar:
    print(name, score)