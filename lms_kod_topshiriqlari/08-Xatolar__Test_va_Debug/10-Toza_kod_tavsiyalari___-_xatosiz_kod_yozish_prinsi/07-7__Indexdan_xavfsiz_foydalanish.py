n = int(input())
lst = [input() for _ in range(n)]
idx = int(input())
if 0 <= idx < len(lst):
    print(lst[idx])
else:
    print("OUT")