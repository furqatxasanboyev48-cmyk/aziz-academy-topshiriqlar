n = int(input())
parts = input().split()
s = 0
for p in parts:
    x = int(p)
    if x > 0 and x < 10:
        print(x)