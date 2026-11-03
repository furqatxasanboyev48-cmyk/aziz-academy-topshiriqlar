def join3(a, b='-', c='-'):
    return a + " " + b + " " + c
qator = input().split()
if len(qator) == 1:
    print(join3(qator[0]))
elif len(qator) == 2:
    print(join3(qator[0], qator[1]))
else:
    print(join3(qator[0], qator[1], qator[2]))