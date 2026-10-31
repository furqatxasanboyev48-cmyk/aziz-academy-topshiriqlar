n = int(input())
rows = []
for _ in range(n):
    key, value = input().split()
    rows.append((key, int(value)))
print("{:<12} | {:>12}".format("Key", "Value"))
print("-" * 12 + "+" + "-" * 12)
for key, value in rows:
    print("{:<12} | {:>11}".format(key, value))