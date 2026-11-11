import csv
n = int(input())
rows = []
for _ in range(n):
    product, qty, price = input().split()
    rows.append([product, qty, price])
with open("c6.csv", "w", newline="") as f:
    yozgich = csv.writer(f)
    for row in rows:
        yozgich.writerow(row)
total = 0
with open("c6.csv", "r", newline="") as f:
    for row in csv.reader(f):
        total += int(row[1]) * int(row[2])
print(total)