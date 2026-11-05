def pc(n):
    if n == 0:
        return 0
    return n % 2 + pc(n // 2)
print(pc(int(input())))