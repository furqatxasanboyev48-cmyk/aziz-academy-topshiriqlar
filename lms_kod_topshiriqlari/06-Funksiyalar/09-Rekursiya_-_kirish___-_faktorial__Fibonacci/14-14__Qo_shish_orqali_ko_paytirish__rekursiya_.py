def m(a, b):
    if b == 0:
        return 0
    return a + m(a, b - 1)
a, b = map(int, input().split())
print(m(a, b))