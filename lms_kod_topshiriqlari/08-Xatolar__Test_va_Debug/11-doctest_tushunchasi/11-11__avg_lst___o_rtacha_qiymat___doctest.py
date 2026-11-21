def avg(lst):
    if not lst:
        return 0.0
    return sum(lst) / len(lst)
import doctest
doctest.testmod()
n= int(input())
lst = [int(input()) for _ in range(n)]
print(f"{avg(lst):.2f}")