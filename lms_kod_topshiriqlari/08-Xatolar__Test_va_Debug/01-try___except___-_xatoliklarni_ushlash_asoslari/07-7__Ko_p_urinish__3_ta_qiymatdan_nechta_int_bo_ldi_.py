count = 0
for _ in range(3):
    s = input()
    try:
        int(s)
        count += 1
    except ValueError:
        pass
print(count)