while True:
    line = input()
    if line.strip() == "0":
        print("Exit")
        break
    parts = line.split()
    a = int(parts[0])
    b = int(parts[1])
    tanlov = int(input())
    if tanlov == 1:
        print(a + b)
    elif tanlov == 2:
        print(a - b)
    elif tanlov == 3:
        print(a * b)
    elif tanlov == 4:
        print(a / b)