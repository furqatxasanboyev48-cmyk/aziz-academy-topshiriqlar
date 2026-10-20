n = int(input())
parts = input().split()
s = 0
for p in parts:
    x = int(p)
    if x > 0:
        s += x
print(s)