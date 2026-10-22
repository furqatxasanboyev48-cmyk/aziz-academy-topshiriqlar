parts = input().split()
n = int(parts[0])
m = int(parts[1])
for j in range(1, m + 1):
    s = 0
    for i in range(1, n + 1):
        s += i * j
    print(s)