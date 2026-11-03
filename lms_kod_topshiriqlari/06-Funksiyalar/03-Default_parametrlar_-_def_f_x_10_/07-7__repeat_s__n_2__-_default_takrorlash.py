def repeat(s, n=2):
    return s * n 
s = input()
qator = input().strip()
if qator:
    print(repeat(s, int(qator)))
else:
    print(repeat(s))