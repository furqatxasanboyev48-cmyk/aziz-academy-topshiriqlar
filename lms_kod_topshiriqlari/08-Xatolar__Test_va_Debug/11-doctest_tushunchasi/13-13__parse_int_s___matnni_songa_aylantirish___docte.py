def parse_int(s):
    return int(s)
import doctest
doctest.testmod()
s = input().strip()
try:
    print(parse_int(s))
except ValueError:
    print("BAD")
