n = int(input())
try:
    assert n >= 10
except AssertionError:
    print("SMALL")
else:
    print("OK")