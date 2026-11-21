def max_of_two(a, b):
    return a if a > b else b 
import doctest
doctest.testmod()
a, b = map(int, input().split())
print(max_of_two(a, b))