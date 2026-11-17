n = int(input())
try:
    assert n > 0
except AssertionError:
    print("ERROR")
else:
    print("OK")