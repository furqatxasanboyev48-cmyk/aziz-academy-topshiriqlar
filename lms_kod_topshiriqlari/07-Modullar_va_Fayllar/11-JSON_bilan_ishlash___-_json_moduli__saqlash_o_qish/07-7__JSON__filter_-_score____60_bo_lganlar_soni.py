import json
n = int(input())
talabalar = []
for _ in range(n):
    name, score = input().split()
    talabalar.append({"name": name, "score": int(score)})
text = json.dumps(talabalar)
qayta = json.loads(text)
count = 0
for t in qayta:
    if t["score"] >= 60:
        count += 1
print(count)
    
