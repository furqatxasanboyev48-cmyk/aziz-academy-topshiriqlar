n = int(input())
rows = []
for _ in range(n):
    name, score = input().split()
    rows.append((name, int(score)))
print("{:<10} | {:>5}".format("Name", "Score"))
print("-" * 10 + "+" + "-" * 5)
for name, score in rows:
    print("{:<10} | {:>5}".format(name, score))