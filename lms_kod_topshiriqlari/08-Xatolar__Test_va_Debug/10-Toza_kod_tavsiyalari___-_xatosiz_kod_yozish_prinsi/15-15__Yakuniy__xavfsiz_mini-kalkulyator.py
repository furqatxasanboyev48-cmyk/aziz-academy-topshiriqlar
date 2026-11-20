command = input().strip()
a = input().strip()
b = input().strip()
try:
    x = int(a)
    y = int(b)
    if command == "ADD":
        print(x + y)
    elif command == "DIV":
        if y == 0:
            print("DIV0")
        else:
            print(x // y)
    else:
        print("BAD")
except ValueError:
    print("BAD")
        