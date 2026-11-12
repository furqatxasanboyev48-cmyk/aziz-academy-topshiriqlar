import json
name = input()
score = int(input())
obj = {"name": name, "score": score}
with open("j4.json", "w", encoding="utf-8") as f:
    json.dump(obj, f, ensure_ascii=False, sort_keys=True)
with open("j4.json", "r", encoding="utf-8") as f:
    qayta = json.load(f)
print(f"{qayta["name"]} {qayta["score"]}")