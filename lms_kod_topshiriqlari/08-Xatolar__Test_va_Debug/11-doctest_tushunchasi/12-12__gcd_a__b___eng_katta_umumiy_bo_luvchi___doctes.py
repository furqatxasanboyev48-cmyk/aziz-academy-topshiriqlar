def gcd(a, b):
    while b:
        a, b = b, a % b 
    return a 
import doctest
doctest.testmod()
a, b = map(int, input().split())
print(gcd(a, b))