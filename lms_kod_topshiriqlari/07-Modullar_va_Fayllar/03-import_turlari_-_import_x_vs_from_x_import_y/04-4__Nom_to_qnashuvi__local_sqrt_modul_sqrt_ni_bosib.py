def butun_ildiz(n):
    r = 0
    while (r + 1) * (r + 1) <= n:
        r += 1
    return r 
math_mod = {"sqrt": butun_ildiz}
n = int(input())
print(math_mod["sqrt"](n))