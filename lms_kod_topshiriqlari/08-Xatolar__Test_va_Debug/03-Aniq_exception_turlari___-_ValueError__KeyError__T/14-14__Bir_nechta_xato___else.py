a = input()
b = input()
try:
    r = int(a) + int(b)
except ValueError:
    print("BAD")
except TypeError:
    print("TYPE")
else:
    print("OK")