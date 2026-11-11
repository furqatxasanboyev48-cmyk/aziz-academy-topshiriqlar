import csv
n = int(input())
rows = []
for _ in range(n):
    name, score = input().split()
    rows.append([name, score])
with open("c9.csv", "w", newline="") as f:
    yozgich = csv.writer(f, delimiter=";")
    for row in rows:
        yozgich.writerow(row)
max_score = None
with open("c9.csv", "r", newline="") as f:
    for row in csv.reader(f, delimiter=";"):
        score = int(row[1])
        if max_score is None or score > max_score:
            max_score = score
print(max_score)
        
    