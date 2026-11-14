n = int(input())
lst = [input() for _ in range(n)]
idx = int(input())
try:
    print(lst[idx])
except IndexError:
    print("OUT")
    