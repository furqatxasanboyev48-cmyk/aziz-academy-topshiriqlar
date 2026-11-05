def rev(n, acc=0):
    if n == 0:
        return acc 
    return rev(n // 10, acc * 10 + n % 10)
print(rev(int(input())))