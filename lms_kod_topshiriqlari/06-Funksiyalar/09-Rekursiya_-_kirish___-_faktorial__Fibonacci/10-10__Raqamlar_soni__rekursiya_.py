def cd(n):
    if n < 10:
        return 1 
    return 1 + cd(n // 10)
print(cd(int(input())))
    