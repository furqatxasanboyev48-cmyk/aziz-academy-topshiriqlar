def dr(n):
    if n < 10:
        return n 
    s = 0
    while n:
        s += n % 10
        n //= 10
    return dr(s)
print(dr(int(input())))