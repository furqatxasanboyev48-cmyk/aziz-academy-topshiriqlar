password = input()
try:
    assert len(password) >= 6
except AssertionError:
    print("WEAK")
else:
    print("OK")

