s = input()
try:
    int(s)
except ValueError:
    print("BAD")
else:
    print("OK")