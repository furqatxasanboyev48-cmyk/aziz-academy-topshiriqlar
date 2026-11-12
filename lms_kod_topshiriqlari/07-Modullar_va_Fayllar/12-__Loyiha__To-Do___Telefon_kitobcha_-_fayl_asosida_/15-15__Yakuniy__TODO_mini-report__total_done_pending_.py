import json
n = int(input())
tasks = []
for _ in range(n):
    title, done = input().split()
    tasks.append({"title": title, "done": done == "1"})
with open("todo15.json", "w", encoding="utf-8") as f:
    json.dump(tasks, f, ensure_ascii=False)
with open("todo15.json", "r", encoding="utf-8") as f:
    tasks = json.load(f)
total = len(tasks)
done_count = 0
for task in tasks:
    if task["done"]:
        done_count += 1
pending = total - done_count
print("total", total)
print("done", done_count)
print("pending", pending)
    