def inc(x, step=1):
    return x + step
qator = input().split()
if len(qator) == 1:
    print(inc(int(qator[0])))
else:
    print(inc(int(qator[0]), int(qator[1])))
