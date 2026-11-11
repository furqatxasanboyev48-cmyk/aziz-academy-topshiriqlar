import csv
n = int(input())
rows = []
for _ in range(n):
    name, score = input().split()
    rows.append([name, score])
with open("c4.csv", "w", newline="") as f:
    yozgich = csv.writer(f)
    for row in rows:
        yozgich.writerow(row)
balllar = []
with open("c4.csv", "r", newline="") as f:
    for row in csv.reader(f):
        balllar.append(int(row[1]))
print(f"{sum(balllar) / len(balllar):.2f}")