parts = input().split()
a = int(parts[0])
b = int(parts[1])
m = a
if b < m:
    m = b
g = 1
for i in range(1, m + 1):
    if a % i == 0 and b % i == 0:
        g = i
print(g)
