import json
n = int(input())
tasks = []
for _ in range(n):
    title, done = input().split()
    tasks.append({"title": title, "done": done == "1"})
with open("todo8.json", "w", encoding="utf-8") as f:
    json.dump(tasks, f, ensure_ascii=False)
with open("todo8.json", "r", encoding="utf-8") as f:
    tasks = json.load(f)
done_count = 0
for task in tasks:
    if task["done"]:
        done_count += 1
print(done_count)
    
    