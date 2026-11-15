n = int(input())
total = 0
for _ in range(n):
    s = input()
    try:
        total += int(s)
    except ValueError:
        pass
print(total)