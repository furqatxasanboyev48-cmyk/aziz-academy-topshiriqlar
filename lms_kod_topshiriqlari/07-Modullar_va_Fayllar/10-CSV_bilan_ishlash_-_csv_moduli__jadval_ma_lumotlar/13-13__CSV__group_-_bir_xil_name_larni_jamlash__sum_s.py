import csv
n = int(input())
rows = []
for _ in range(n):
    name, score = input().split()
    rows.append([name, score])
with open("c13.csv", "w", newline="") as f:
    yozgich = csv.writer(f)
    for row in rows:
        yozgich.writerow(row)
jamlanma = {}
with open("c13.csv", "r", newline="") as f:
    for row in csv.reader(f):
        name = row[0]
        score = int(row[1])
        if name in jamlanma:
            jamlanma[name] += score
        else:
            jamlanma[name] = score
for name in sorted(jamlanma):
    print(name, jamlanma[name])

    
        