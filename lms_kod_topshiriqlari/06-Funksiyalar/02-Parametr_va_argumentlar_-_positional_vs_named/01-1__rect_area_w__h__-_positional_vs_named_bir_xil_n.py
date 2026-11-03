def rect_area(w, h):
    return w * h
qator = input().split()
w = int(qator[0])
h = int(qator[1])
print(rect_area(w, h))
print(rect_area(h=h, w=w))