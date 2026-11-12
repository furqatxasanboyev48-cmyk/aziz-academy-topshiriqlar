import json
n = int(input())
tasks = []
for _ in range(n):
    title, done = input().split()
    tasks.append({"title": title, "done": done == "1"})
sub = input().strip()
with open("todo12.json", "w", encoding="utf-8") as f:
    json.dump(tasks, f, ensure_ascii=False)
with open("todo12.json", "r", encoding="utf-8") as f:
    tasks = json.load(f)
for task in tasks:
    if sub in task["title"]:
        print(task["title"])
        