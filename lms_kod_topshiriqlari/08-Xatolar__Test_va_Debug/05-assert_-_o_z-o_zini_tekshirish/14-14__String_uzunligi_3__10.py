s = input()
try:
    assert 3 <= len(s) <= 10
except AssertionError:
    print("ERROR")
else:
    print("OK")