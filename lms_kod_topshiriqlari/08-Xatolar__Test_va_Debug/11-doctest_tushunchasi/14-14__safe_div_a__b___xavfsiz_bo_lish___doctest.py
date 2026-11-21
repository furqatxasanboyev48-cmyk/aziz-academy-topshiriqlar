def safe_div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b 
import doctest
doctest.testmod()
a, b = map(int, input().split())
try:
    print(f"{safe_div(a, b):.2f}")
except ZeroDivisionError:
    print("DIV0")