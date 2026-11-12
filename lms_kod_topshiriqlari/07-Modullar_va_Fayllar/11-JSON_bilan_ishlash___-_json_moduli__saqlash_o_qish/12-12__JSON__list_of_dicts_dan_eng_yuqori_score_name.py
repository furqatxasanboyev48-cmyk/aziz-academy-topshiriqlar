import json
n = int(input())
talabalar = []
for _ in range(n):
    name, score = input().split()
    talabalar.append({"name": name, "score": int(score)})
text = json.dumps(talabalar)
qayta = json.loads(text)
best = None
for t in qayta:
    if best is None or t["score"] > best["score"]:
        best = t 
print(best["name"])