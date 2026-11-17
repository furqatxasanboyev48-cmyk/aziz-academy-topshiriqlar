score = int(input())
try:
    assert 0 <= score <= 100
except AssertionError:
    print("OUT")
else:
    print("OK")