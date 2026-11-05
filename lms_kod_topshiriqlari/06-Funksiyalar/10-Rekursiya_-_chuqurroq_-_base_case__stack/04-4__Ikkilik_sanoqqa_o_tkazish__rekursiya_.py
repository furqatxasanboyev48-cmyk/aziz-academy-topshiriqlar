def b(n):
    if n < 2:
        return str(n)
    return b(n // 2) + str(n % 2)
print(b(int(input())))