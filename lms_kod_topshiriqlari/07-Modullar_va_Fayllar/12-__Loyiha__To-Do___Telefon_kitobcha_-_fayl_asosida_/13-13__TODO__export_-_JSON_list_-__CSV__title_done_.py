import csv
import json
n = int(input())
tasks = []
for _ in range(n):
    title, done = input().split()
    tasks.append({"title": title, "done": int(done)})
with open("todo13.json", "w", encoding="utf-8") as f:
    json.dump(tasks, f, ensure_ascii=False)
with open("todo13.json", "r", encoding="utf-8") as f:
    tasks = json.load(f)
with open("todo13.csv", "w", newline="") as f:
    yozgich = csv.writer(f, delimiter=",")
    for task in tasks:
        yozgich.writerow([task["title"], task["done"]])
done_count = 0
with open("todo13.csv", "r", newline="") as f:
    for row in csv.reader(f):
        if row[1] == "1":
            done_count += 1
print(done_count)
    
    
