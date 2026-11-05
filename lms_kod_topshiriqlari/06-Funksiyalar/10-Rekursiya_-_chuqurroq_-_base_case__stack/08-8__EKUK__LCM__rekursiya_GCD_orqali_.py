def g(a, b):
    return a if b == 0 else g(b, a % b)
a, b = map(int, input().split())
print(a * b // g(a, b))