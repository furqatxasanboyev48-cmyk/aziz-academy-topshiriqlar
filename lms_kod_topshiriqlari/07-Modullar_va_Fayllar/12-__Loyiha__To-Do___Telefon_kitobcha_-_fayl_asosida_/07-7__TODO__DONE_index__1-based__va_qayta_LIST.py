import json
title1 = input()
title2 = input()
k = int(input())
tasks = [
    {"title": title1, "done": False},
    {"title": title2, "done": False},
]
with open("todo7.json", "w", encoding="utf-8") as f:
    json.dump(tasks, f, ensure_ascii=False)
with open("todo7.json", "r", encoding="utf-8") as f:
    tasks = json.load(f)
tasks[k - 1]["done"] = True
with open("todo7.json", "w", encoding="utf-8") as f:
    json.dump(tasks, f, ensure_ascii=False)
with open("todo7.json", "r", encoding="utf-8") as f:
    tasks = json.load(f)
i = 1
for task in tasks:
    if task["done"]:
        belgi = "[x]"
    else:
        belgi = "[ ]"
    print(f"{i}) {task["title"]} {belgi}")
    i += 1