s = input().strip()
try:
    print(int(s))
except ValueError:
    print("ERR")