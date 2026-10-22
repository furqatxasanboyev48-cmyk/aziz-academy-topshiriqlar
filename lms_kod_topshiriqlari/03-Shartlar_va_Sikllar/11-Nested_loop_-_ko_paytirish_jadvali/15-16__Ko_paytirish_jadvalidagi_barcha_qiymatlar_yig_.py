n = int(input())
s = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        s += i * j
print(s)