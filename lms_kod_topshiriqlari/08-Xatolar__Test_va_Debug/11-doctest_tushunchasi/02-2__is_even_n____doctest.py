def is_even(n):
    return n % 2 == 0
import doctest
doctest.testmod()
n = int(input())
print("EVEN" if is_even(n) else "ODD")