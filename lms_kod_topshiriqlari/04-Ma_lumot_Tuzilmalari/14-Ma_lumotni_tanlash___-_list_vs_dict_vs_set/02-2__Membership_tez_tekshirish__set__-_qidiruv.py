n = int(input())
sonlar = set(map(int, input().split()))
q = int(input())
for _ in range(q):
    x = int(input())
    if x in sonlar:
        print("YES")
    else:
        print("NO")