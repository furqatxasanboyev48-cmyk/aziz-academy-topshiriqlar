op = input().strip()
try:
    a = float(input())
    b = float(input())
    if op == "ADD":
        r = a + b 
    elif op == "SUB":
        r = a - b 
    elif op == "MUL":
        r = a * b 
    elif op == "DIV":
        r = a / b 
    else:
        raise Exception("bad op")
except ValueError:
    print("BAD")
except ZeroDivisionError:
    print("DIV0")
except Exception:
    print("OPERR")
else:
    print(f"{r:.2f}")
        