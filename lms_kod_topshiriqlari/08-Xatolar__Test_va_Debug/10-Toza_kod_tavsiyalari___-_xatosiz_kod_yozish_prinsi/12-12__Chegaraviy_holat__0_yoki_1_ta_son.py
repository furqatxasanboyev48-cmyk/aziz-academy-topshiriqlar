n = int(input())
lst = [int(input()) for _ in range(n)]
if n == 0:
    print(0)
elif n == 1:
    print(lst[0])
else:
    print(max(lst) - min(lst))