import math
a,b = map(int, input().split())
if a == 0 or b == 0:
    print(0)
else:
    print(abs(a*b)// math.gcd(a,b))