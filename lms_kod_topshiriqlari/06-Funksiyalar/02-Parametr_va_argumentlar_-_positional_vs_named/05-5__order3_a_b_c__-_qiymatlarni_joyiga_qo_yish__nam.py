def order3(a, b, c):
    return f"a={a} b={b} c={c}"
qator = input().split()
x = int(qator[0])
y = int(qator[1])
z = int(qator[2])
print(order3(x, y, z))
print(order3(c=x, b=y, a=z))