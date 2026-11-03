def rect_area(w, h=1):
    return w * h
qator = input().split()
if len(qator) == 1:
    print(rect_area(int(qator[0])))
else:
    print(rect_area(int(qator[0]), int(qator[1])))