a = input()
b = input()
try:
    print(int(a) + int(b))
except ValueError:
    print("ERROR")