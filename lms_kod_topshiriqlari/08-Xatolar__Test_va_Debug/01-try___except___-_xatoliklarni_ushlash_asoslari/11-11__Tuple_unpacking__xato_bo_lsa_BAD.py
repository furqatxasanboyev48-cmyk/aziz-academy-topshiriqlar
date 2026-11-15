s = input()
try:
    a, b = s.split()
    print(a + "|" + b)
except ValueError:
    print("BAD")