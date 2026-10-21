n = int(input())
parts = input().split()
lst = []
s = 0
for p in parts:
    x = int(p)
    lst.append(x)
    s += x
avg = s / n
c = 0
for x in lst:
    if x > avg:
        c += 1
print(c)
    