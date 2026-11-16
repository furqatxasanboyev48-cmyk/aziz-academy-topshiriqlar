op = input().strip()
a = input()
b = input()
attempts = 0
try:
    a = float(a)
    b = float(b)
    if op == "ADD":
        r = a + b 
    elif op == "SUB":
        r = a - b 
    elif op == "MUL":
        r = a * b 
    else:
        r = a / b 
except ValueError:
        out = "BAD"
except ZeroDivisionError:
    out = "DIV0"
else:
    out= f"{r:.2f}"
finally:
    attempts += 1
print(out)
print(attempts)
        