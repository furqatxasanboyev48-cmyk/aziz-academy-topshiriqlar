n = int(input())
parts = input().split()
c = 0
for p in parts:
    if int(p) > 0:
        c += 1
print(c)