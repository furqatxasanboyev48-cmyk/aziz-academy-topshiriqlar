def st(n):
    if n == 0:
        return ""
    return "*" + st(n - 1)
print(st(int(input())))