n = int(input())
best = 0
for i in range(1, n):
    if n % i == 0:
        best = i
print(best)