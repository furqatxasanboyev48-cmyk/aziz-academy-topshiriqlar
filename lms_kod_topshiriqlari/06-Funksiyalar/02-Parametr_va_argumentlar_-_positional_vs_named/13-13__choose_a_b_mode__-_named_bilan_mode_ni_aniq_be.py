def choose(a, b, mode):
    if mode == "max":
        return max(a, b)
    if mode == "min":
        return min(a, b)
    return a 
qator = input().split()
a = int(qator[0])
b = int(qator[1])
mode = input().strip()
print(choose(a, b, mode))
print(choose(mode=mode, a=a, b=b))
    