import csv
n = int(input())
rows = []
for _ in range(n):
    name, score = input().split()
    rows.append([name, score])
with open("c1.csv", "w", newline="") as f:
    yozgich = csv.writer(f)
    for row in rows:
        yozgich.writerow(row)
with open("c1.csv", "r", newline="") as f:
    for row in csv.reader(f):
        print(row[0], row[1])
    