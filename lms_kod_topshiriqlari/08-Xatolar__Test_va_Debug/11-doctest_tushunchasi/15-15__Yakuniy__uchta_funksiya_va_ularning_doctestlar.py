import sys
def add(a, b):
    return a + b 
def is_palindrome(s):
    return s == s[::-1]
def clamp(x):
    if x < 0:
        return 0 
    if x > 100:
        return 100
    return x 
import doctest
doctest.testmod()
data = sys.stdin.read().split("\n")
op = data[0].strip()
if op == "ADD":
    print(add(int(data[1]), int(data[2])))
elif op == "PAL":
    print("YES" if is_palindrome(data[1].strip()) else "NO")
else:
    print(clamp(int(data[1])))

        