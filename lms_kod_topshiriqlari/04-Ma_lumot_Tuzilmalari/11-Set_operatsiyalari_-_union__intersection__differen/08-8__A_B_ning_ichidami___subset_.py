a = set(map(int, input().split()))
b = set(map(int, input().split()))
if a.issubset(b):
    print("YES")
else:
    print("NO")
    