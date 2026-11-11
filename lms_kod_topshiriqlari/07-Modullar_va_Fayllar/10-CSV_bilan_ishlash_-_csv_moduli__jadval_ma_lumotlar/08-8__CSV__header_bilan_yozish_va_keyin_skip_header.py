import csv
n = int(input())
rows = []
for _ in range(n):
    name, score = input().split()
    rows.append([name, score])
with open("c8.csv", "w", newline="") as f:
    yozgich = csv.writer(f)
    yozgich.writerow(["name", "score"])
    for row in rows:
        yozgich.writerow(row)
jami = 0
with open("c8.csv", "r", newline="") as f:
    oqigich = csv.reader(f)
    birinchi = True
    for row in oqigich:
        if birinchi:
            birinchi = False
            continue
        jami += int(row[1])
print(jami)
    