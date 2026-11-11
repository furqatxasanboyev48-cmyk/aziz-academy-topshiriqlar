import csv
n = int(input())
rows = []
for _ in range(n):
    name, score = input().split()
    rows.append([name, score])
with open("c2.csv", "w", newline="") as f:
    yozgich = csv.writer(f)
    for row in rows:
        yozgich.writerow(row)
jami = 0
with open("c2.csv", "r", newline="") as f:
    for row in csv.reader(f):
        jami += int(row[1])
print(jami)