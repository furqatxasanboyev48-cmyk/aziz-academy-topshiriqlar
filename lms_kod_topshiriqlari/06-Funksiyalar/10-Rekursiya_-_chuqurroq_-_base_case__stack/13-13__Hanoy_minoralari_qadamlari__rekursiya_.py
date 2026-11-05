def h(n):
    if n == 0:
        return 0
    return 2 * h(n - 1) + 1
print(h(int(input())))