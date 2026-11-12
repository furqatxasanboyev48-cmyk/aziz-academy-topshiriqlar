import json
n = int(input())
talabalar = []
for _ in range(n):
    name, score = input().split()
    talabalar.append({"name": name, "score": int(score)})
with open("j6.json", "w", encoding="utf-8") as f:
    json.dump(talabalar, f, ensure_ascii=False)
with open("j6.json", "r", encoding="utf-8") as f:
    qayta = json.load(f)
jami = 0
for t in qayta:
    jami += t["score"]
print(jami)