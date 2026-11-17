op = input().strip()
try:
    assert op in ("ADD", "SUB")
except AssertionError:
    print("OPERR")
else:
    print("OK")