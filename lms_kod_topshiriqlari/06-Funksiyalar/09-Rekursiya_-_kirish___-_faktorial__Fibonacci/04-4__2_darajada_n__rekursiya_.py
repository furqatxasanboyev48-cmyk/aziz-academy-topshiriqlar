def p(n):
    if n == 0:
        return 1
    return 2 * p(n - 1)
print(p(int(input())))
        