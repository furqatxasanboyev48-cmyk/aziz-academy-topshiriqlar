def reverse_str(s):
    return s[::-1]
import doctest
doctest.testmod()
s = input().strip()
print(reverse_str(s))