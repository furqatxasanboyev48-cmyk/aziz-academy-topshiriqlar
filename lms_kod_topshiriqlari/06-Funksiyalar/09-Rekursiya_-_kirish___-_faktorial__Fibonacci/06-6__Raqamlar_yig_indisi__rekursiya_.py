def ds(n):
    if n < 10:
        return n 
    return n % 10 + ds(n // 10)
print(ds(int(input())))
    