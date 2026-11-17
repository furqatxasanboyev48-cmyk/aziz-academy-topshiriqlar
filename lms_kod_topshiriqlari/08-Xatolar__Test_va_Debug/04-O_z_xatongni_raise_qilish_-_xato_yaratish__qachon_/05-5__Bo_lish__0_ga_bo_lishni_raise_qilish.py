a = int(input())
b = int(input())
try:
    if b == 0:
        raise ZeroDivisionError
    print(a // b)
except ZeroDivisionError:
    print("DIV0")