n = int(input())
try:
    assert n % 2 == 0
except AssertionError:
    print("ODD")
else:
    print("EVEN")