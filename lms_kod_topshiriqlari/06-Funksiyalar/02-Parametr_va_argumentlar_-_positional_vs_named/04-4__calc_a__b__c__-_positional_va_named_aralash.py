def calc(a, b, c):
    return a + b * c 
qator = input().split()
a = int(qator[0])
b = int(qator[1])
c = int(qator[2])
print(calc(a, b, c))
print(calc(a, c=c, b=b))
