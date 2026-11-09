import math
a, b, c = map(float, input().split())
D = b * b - 4 * a * c 
if D < 0:
    print("NO")
elif D == 0:
    x = -b / (2 * a) + 0.0
    print(f"{x:.4f}")
else:
    x1 = (-b - math.sqrt(D)) / (2 * a)
    x2 = (-b + math.sqrt(D)) / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
    print(f"{x1:.4f} {x2:.4f}")
    