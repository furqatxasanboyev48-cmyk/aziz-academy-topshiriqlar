parts = input().split()
n = int(parts[0])
m = int(parts[1])
c = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (i * j) % 2 == 0:
            c += 1
print(c)
        