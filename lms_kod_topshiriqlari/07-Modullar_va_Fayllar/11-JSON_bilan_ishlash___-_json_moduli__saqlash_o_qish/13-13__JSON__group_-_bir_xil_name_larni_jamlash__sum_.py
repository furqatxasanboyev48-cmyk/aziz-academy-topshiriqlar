import json
n = int(input())
jamlanma = {}
for _ in range(n):
    name, score = input().split()
    if name in jamlanma:
        jamlanma[name] += int(score)
    else:
        jamlanma[name] = int(score)
print(json.dumps(jamlanma, ensure_ascii=False, sort_keys=True))