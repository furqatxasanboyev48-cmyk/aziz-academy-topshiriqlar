n = int(input())
lst = [input() for _ in range(n)]
try:
    assert n > 0
except AssertionError:
    print("EMPTY")
else:
    print("OK")