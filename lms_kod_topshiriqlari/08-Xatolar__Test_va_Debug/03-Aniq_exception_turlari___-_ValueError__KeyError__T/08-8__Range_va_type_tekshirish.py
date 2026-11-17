s = input()
try:
    n = int(s)
except ValueError:
    print("BAD")
else:
    if n < 0 or n > 100:
        print("OUT")
    else:
        print("OK")