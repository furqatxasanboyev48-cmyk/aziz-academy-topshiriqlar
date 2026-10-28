a = set(map(int, input().split()))
b = set(map(int, input().split()))
farq = b - a
if farq:
    print(" ".join(str(x) for x in sorted(farq)))
else:
    print("BO'SH")