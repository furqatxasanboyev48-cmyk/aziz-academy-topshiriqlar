parts = input().split()
a = int(parts[0])
b = int(parts[1])
c = int(parts[2])
if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if b >= c:
        print(b)
    else:
        print(c)
    