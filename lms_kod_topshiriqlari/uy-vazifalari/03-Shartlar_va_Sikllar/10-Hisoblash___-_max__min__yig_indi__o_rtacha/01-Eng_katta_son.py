n = int(input())
mx = int(input())
for i in range(n - 1):
    x = int(input())
    if x > mx:
        mx = x
print(mx)