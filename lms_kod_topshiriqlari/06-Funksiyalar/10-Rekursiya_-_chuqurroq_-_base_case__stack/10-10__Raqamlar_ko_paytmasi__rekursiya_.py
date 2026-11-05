def dp(n):
    if n < 10:
        return n 
    return (n % 10) * dp(n // 10)
print(dp(int(input())))