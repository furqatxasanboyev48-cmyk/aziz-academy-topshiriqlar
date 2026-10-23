parts = input().split()
a = int(parts[0])
b = int(parts[1])
tanlov = input()
if tanlov == "add":
    print(a + b)
elif tanlov == "sub":
    print(a - b)
elif tanlov == "mul":
    print(a * b)
elif tanlov == "div":
    print(a / b)