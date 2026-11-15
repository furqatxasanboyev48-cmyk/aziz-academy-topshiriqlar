n = int(input())
first = int(input())
mx = first
mn = first
for i in range(n - 1):
    x = int(input())
    if x > mx:
        mx = x
    if x < mn:
        mn = x
print(mx - mn)