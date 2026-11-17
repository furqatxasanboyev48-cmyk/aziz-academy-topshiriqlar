a = int(input())
b = int(input())
try:
    assert b > a 
except AssertionError:
    print("ERROR")
else:
    print("OK")