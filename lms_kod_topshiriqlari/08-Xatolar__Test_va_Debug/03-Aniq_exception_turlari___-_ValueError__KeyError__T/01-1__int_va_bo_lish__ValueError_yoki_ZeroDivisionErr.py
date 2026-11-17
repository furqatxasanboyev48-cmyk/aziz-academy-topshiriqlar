a = input()
b = input()
try:
    a = int(a)
    b = int(b)
    print(a // b)
except ValueError:
    print("BAD")
except ZeroDivisionError:
    print("DIV0")
    