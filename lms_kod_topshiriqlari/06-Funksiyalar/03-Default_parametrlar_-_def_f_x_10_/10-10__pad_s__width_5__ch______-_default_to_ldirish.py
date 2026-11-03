def pad(s, width=5, ch='.'):
    if len(s) >= width:
        return s 
    return s + ch * (width - len(s))
s = input()
qator = input().split()
if len(qator) == 0:
    print(pad(s))
elif len(qator) == 1:
    print(pad(s, int(qator[0])))
else:
    print(pad(s, int(qator[0]), qator[1]))