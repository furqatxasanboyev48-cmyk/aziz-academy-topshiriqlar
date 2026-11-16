n = int(input())
lst = [input() for _ in range(n)]
idx = int(input())
try:
    lst[idx]
except IndexError:
    print("OUT")
else:
    print("OK")
    