def power(a, b):
    return a ** b 
qator = input().split()
a = int(qator[0])
b = int(qator[1])
print(power(a, b))
print(power(b=b, a=a))