n = int(input())
rows = []
for _ in range(n):
    name, score = input().split()
    rows.append((name, int(score)))
print("{:<10} | {:>5}".format("Name", "Score"))
print("-" * 10 + "+" + "-" * 5)
for name, score in rows:
    print("{:<10} | {:>5}".format(name, score))
top = None
for name, score in rows:
    if top is None or score > top[1] or (score == top[1] and name < top[0]):
        top = (name, score)
print("TOP: {} {}".format(top[0], top[1]))
    