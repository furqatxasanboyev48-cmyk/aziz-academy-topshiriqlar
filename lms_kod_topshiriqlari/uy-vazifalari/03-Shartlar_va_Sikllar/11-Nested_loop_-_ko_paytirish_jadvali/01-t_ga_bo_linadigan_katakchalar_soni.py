n = int(input())
t = int(input())
count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i*j) % t == 0:
            count += 1
print(count)