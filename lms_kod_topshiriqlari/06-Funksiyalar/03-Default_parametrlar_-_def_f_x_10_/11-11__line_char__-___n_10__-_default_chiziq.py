def line(char='-', n=10):
    return char * n 
qator = input().split()
if len(qator) == 0:
    print(line())
elif len(qator) == 1:
    if qator[0].isdigit():
        print(line(n=int(qator[0])))
    else:
        print(line(qator[0]))
else:
    print(line(qator[0], int(qator[1])))
    