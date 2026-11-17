fn = input().strip()
try:
    with open(fn) as f:
        print(f.read())
except FileNotFoundError:
    print("NOFILE")
except PermissionError:
    print("NOPERM")
        