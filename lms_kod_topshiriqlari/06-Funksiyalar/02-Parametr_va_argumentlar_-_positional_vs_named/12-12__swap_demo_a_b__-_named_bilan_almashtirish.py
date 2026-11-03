def pair(a, b):
    return f"a={a} b={b}"
qator= input().split()
a = int(qator[0])
b = int(qator[1])
print(pair(a, b))
print(pair(a=b, b=a))