age = int(input())
password = input()
try:
    assert age >= 18
    assert len(password) >= 6
except AssertionError:
    print("REJECT")
else:
    print("ACCEPT")