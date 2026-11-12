import json
n = int(input())
balllar = []
for _ in range(n):
    balllar.append(int(input()))
with open("j15.json", "w", encoding="utf-8") as f:
    json.dump(balllar, f)
with open("j15.json", "r", encoding="utf-8") as f:
    qayta = json.load(f)
print(len(qayta))
print(sum(qayta))
print(f"{sum(qayta) / len(qayta):.2f}")
print(max(qayta))

    