import csv
n = int(input())
rows = []
for _ in range(n):
    product, qty, price = input().split()
    rows.append([product, qty, price])
with open("c7.csv", "w", newline="") as f:
    yozgich = csv.writer(f)
    for row in rows:
        yozgich.writerow(row)
best_product = None
best_qty = None
with open("c7.csv", "r", newline="") as f:
    for row in csv.reader(f):
        qty = int(row[1])
        if best_qty is None or qty > best_qty:
            best_qty = qty
            best_product = row[0]
print(best_product)

        
