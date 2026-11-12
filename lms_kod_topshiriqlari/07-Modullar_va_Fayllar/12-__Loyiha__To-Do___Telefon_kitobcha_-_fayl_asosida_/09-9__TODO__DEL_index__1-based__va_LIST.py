import json 
title1 = input()
title2 = input()
title3 = input()
k = int(input())
tasks = [
    {"title": title1, "done": False},
    {"title": title2, "done": False},
    {"title": title3, "done": False},
    
]
with open("todo9.json", "w", encoding="utf-8") as f:
    json.dump(tasks, f, ensure_ascii=False)
with open("todo9.json", "r", encoding="utf-8") as f:
    tasks = json.load(f)
del tasks[k - 1]
i = 1
for task in tasks:
    if task["done"]:
        belgi = "[x]"
    else:
        belgi = "[ ]"
    print(f"{i}) {task["title"]} {belgi}")
    i += 1
        
    