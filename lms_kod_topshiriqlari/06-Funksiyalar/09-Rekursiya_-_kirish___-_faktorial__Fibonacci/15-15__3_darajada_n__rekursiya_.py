def p3(n):
    if n == 0:
        return 1 
    return 3 * p3(n - 1)
print(p3(int(input())))