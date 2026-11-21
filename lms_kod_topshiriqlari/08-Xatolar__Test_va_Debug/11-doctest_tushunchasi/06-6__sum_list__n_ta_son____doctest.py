def sum_list(lst):
    return sum(lst)
import doctest
doctest.testmod()
n = int(input())
lst = [int(input()) for _ in range(n)]
print(sum_list(lst))