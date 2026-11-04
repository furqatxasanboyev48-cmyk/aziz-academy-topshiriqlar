def slice_text(s, start=0, end=None):
    return s[start:end]
s = input()
qator = input().split()
if len(qator) == 0:
    print(slice_text(s))
elif len(qator) == 1:
    print(slice_text(s, int(qator[0])))
else:
    print(slice_text(s, int(qator[0]), int(qator[1])))