op = input().strip()
try:
    a = float(input())
    b = float(input())
    if op == "ADD":
        print(f"{a + b:.2f}")
    elif op == "SUB":
        print(f"{a - b:.2f}")
    elif op == "SUB":
        print(f"{a - b:.2f}")
    elif op == "MUL":
        print(f"{a * b:.2f}")
    elif op == "DIV":
        print(f"{a / b:.2f}")
    else:
        print("OPERR")
except ValueError:
    print("BAD")
except ZeroDivisionError:
    print("DIV0")