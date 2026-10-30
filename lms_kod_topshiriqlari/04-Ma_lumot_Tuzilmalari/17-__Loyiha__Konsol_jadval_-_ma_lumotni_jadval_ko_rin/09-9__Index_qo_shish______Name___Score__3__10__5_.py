n = int(input())
rows = []
for _ in range(n):
    name, score = input().split()
    rows.append((name, int(score)))
i = 1
for name, score in rows:
    print("{}|{}|{}".format(i, name, score))
    i += 1
    