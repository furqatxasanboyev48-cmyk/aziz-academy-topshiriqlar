def uniq_count(lst):
    return len(set(lst))
import doctest
doctest.testmod()
n = int(input())
lst = [int(input()) for _ in range(n)]
print(uniq_count(lst))