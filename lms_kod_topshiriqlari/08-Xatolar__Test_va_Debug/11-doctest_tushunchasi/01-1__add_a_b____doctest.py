def add(a, b):
    return a + b 
import doctest
doctest.testmod()
a, b = map(int, input().split())
print(add(a, b))