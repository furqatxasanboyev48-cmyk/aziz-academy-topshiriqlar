n = int(input())
mn = int(input())
for i in range(n - 1):
    x = int(input())
    if x < mn:
        mn = x
print(mn)