def t(n):
    if n == 1:
        return "1"
    return str(n) + " " + t(n - 1)
print(t(int(input())))