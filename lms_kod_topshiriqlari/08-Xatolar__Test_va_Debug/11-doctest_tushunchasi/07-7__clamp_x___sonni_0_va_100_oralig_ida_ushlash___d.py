def clamp(x):
    if x < 0:
        return 0 
    if x > 100:
        return 100
    return x 
import doctest
doctest.testmod()
x = int(input())
print(clamp(x))