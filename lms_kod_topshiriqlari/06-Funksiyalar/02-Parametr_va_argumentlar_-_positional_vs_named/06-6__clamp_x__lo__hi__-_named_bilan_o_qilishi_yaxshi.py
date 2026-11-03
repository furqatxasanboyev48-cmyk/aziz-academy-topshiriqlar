def clamp(x, lo, hi):
    if x < lo:
        return lo 
    if x > hi:
        return hi
    return x
qator = input().split()
x = int(qator[0])
lo = int(qator[1])
hi = int(qator[2])
print(clamp(x, lo, hi))
print(clamp(lo=lo, hi=hi, x=x))
