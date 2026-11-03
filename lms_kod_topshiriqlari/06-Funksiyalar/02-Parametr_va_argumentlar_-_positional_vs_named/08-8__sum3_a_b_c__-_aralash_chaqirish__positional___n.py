def sum3(a, b, c):
    return a + b + c 
qator = input().split()
a = int(qator[0])
b = int(qator[1])
c = int(qator[2])
print(sum3(a, b, c))
print(sum3(a, b=b, c=c))


