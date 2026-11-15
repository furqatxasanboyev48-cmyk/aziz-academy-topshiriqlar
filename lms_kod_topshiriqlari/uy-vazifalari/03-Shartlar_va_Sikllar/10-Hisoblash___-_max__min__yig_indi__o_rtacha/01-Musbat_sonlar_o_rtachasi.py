n = int(input())
s = 0
c = 0
for i in range(n):
    x = int(input())
    if x > 0:
        s += x 
        c += 1
if c > 0:
        print(s // c)
else:
    print(0)
        
        