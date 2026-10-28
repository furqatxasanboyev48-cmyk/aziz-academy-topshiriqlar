a = set(map(int, input().split()))
b = set(map(int, input().split()))
if a.isdisjoint(b):
    print("YES")
else:
    print("NO")