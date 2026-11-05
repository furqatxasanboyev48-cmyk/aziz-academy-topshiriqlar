def sq(n):
    if n == 0:
        return 0
    return n * n + sq(n - 1)
print(sq(int(input())))