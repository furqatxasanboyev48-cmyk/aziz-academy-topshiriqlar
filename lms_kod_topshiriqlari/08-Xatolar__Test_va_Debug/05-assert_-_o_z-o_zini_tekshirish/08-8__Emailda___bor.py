email = input().strip()
try:
    assert "@" in email
except AssertionError:
    print("BAD")
else:
    print("OK")