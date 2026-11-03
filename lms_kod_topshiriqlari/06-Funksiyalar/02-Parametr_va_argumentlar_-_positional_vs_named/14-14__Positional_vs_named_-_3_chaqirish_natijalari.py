def f(a, b, c):
    return a * 100 + b * 10 + c 
qator = input().split()
a = int(qator[0])
b = int(qator[1])
c = int(qator[2])
print(f(a, b, c))
print(f(c=c, a=a, b=b))
print(f(a=c, b=b, c=a))