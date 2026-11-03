def diff(a, b):
    return a - b 
qator = input().split()
a = int(qator[0])
b = int(qator[1])
print(diff(a, b))
print(diff(b=a, a=b))

