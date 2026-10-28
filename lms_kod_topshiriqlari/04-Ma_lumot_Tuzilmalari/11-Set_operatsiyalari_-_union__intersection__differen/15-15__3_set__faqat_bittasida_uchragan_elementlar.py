A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = set(map(int, input().split()))
yolgiz = (A - B - C) | (B - A - C) | (C - A - B)
if yolgiz:
    print(" ".join(str(x) for x in sorted(yolgiz)))
else:
    print("BO'SH")