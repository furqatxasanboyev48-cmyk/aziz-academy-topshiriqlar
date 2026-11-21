def count_words(s):
    return len(s.split())
import doctest
doctest.testmod()
s = input()
print(count_words(s))