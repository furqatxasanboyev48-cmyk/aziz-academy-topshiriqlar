def is_palindrome(s):
    return s == s[::-1]
import doctest
doctest.testmod()
s = input().strip()
print("YES" if is_palindrome(s) else "NO")