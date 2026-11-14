a = input()
b = input()
try:
    print(f"{float(a) / float(b):.2f}")
except ValueError:
    print("BAD")
except ZeroDivisionError:
    print("DIV0")
    