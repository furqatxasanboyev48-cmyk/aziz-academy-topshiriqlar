age = int(input())
try:
    assert age >= 18
except AssertionError:
    print("DENIED")
else:
    print("ALLOWED")