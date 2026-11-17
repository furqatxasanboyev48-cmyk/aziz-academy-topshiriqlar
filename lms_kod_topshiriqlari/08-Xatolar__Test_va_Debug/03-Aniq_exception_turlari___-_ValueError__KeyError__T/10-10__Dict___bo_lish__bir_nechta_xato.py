n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
a, b = input().split()
try:
    print(d[a] // d[b])
except KeyError:
    print("NOKEY")
except ZeroDivisionError:
    print("DIV0")