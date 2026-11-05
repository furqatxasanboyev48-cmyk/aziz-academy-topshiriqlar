def pw(a, b):
    if b == 0:
        return 1
    return a * pw(a, b - 1)
a, b = map(int, input().split())
print(pw(a, b))