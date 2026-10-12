parts = input().split()
a = int(parts[0])
b = int(parts[1])
op = parts[2]
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
else:
    print("Invalid")