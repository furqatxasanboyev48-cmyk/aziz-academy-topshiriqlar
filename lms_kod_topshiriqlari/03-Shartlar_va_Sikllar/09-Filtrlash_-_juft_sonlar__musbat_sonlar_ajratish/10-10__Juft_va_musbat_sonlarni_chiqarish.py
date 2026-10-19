n = int(input())
parts = input().split()
c = 0
for p in parts:
    x = int(p)
    if x > 0 and x % 2 == 0:
        print(x)
    