s = input()
try:
    try:
        float(s)
    except ValueError:
        raise
except ValueError:
    print("BAD")
else:
    print("OK")
        