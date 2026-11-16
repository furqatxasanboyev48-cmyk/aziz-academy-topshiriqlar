a = int(input())
b = int(input())
try:
    r = a // b 
except ZeroDivisionError:
    print("DIV0")
else:
    print(r)
    