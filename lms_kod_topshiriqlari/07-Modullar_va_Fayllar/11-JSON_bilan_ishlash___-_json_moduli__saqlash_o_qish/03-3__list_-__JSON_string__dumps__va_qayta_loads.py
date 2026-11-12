import json
n = int(input())
sonlar = []
for _ in range(n):
    sonlar.append(int(input()))
text = json.dumps(sonlar)
qayta = json.loads(text)
print(sum(qayta))