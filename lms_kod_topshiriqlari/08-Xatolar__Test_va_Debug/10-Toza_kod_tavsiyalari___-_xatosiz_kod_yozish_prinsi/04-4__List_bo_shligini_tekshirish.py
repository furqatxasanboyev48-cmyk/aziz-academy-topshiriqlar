n = int(input())
lst = [ int(input()) for _ in range(n)]
if not lst:
    print(0)
else:
    print(max(lst))