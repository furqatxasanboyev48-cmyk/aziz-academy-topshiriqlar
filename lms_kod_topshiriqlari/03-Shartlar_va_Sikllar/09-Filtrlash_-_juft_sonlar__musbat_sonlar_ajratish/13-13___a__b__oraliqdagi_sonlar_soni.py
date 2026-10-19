n = int(input())
parts = input().split()
ab = input().split()
a = int(ab[0])
b = int(ab[1])
c = 0
for p in parts:
    x = int(p)
    if a <= x and x <= b:
        c += 1
print(c)