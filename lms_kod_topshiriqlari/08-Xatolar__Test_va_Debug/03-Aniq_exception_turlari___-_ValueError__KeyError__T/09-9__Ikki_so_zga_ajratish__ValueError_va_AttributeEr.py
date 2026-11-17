s = input().strip()
if s == "":
    s = None
try:
    a, b = s.split()
except ValueError:
    print("BAD")
except AttributeError:
    print("TYPE")
else:
    print(a + "|" + b)
    