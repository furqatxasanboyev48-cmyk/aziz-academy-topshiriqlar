def max2(a, b):
    if a > b:
        return a
    return b 
qator = input().split()
a = int(qator[0])
b = int(qator[1])
print(max2(a, b))