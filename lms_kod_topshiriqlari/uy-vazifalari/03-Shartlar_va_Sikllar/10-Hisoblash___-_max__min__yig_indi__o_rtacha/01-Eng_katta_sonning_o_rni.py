n = int(input())
mx = int(input())
pos = 1
for i in range(n - 1):
    x = int(input())
    if x > mx:
        mx = x
        pos = i + 2
print(pos)
    