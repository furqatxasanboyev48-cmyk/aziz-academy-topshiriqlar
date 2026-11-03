def power(a, b=2):
    return a ** b 
qator = input().split()
if len(qator) == 1:
    print(power(int(qator[0])))
else:
    print(power(int(qator[0]), int(qator[1])))