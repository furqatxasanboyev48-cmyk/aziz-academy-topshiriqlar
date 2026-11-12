import json
title1 = input()
title2 = input()
tasks = [
    {"title": title1, "done": False},
    {"title": title2, "done": False},
]
with open("todo6.json", "w", encoding="utf-8") as f:
    json.dump(tasks, f, ensure_ascii=False)
with open("todo6.json", "r", encoding="utf-8") as f:
    tasks = json.load(f)
k = 1
for task in tasks:
    if task["done"]:
        belgi = "[x]"
    else:
        belgi = "[ ]"
    print(f"{k}) {task["title"]} {belgi}")
    k += 1
    