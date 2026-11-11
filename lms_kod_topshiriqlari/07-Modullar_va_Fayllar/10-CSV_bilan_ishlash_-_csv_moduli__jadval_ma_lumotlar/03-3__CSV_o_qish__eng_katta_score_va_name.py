import csv
n = int(input())
rows = []
for _ in range(n):
    name, score = input().split()
    rows.append([name, score])
with open("c3.csv", "w", newline="") as f:
    yozgich = csv.writer(f)
    for row in rows:
        yozgich.writerow(row)
best_name = None
best_score = None
with open("c3.csv", "r", newline="") as f:
    for row in csv.reader(f):
        score = int(row[1])
        if best_score is None or score > best_score:
            best_score = score
            best_name = row[0]
print(best_name, best_score)

    