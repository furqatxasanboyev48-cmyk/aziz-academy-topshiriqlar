s = input()
try:
    assert len(s.strip()) > 0
except AssertionError:
    print("EMPTY")
else:
    print("OK")
    