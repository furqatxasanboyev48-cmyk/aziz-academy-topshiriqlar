n = int(input())
lst = [input() for _ in range(n)]
try:
    if n == 0:
        raise ValueError("bo'sh list")
except ValueError:
    print("EMPTY")
else:
    print("OK")
        