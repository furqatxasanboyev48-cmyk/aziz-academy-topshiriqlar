n = int(input())
p = 0 
m = 0
for i in range(n):
    x = int(input())
    if x > 0:
        p += 1
    elif x < 0:
        m += 1
print(p, m)