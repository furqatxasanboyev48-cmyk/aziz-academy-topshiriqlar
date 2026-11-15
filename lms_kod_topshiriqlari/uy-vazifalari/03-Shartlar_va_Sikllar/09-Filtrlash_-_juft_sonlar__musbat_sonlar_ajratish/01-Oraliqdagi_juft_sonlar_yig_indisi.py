a = int(input())
b = int(input())
s = 0
for x in range(a, b + 1):
    if x % 2 == 0:
        s += x 
print(s)