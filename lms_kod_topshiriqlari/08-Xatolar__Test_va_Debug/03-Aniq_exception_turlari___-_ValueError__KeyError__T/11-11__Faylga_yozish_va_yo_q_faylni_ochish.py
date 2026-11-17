mode = input().strip()
try:
    if mode == "1":
        with open("ex11.txt", "w") as f:
            f.write("ok")
        with open("ex11.txt") as f:
            print(f.read())
    else:
        open("no_such_file_ex11.txt")
except FileNotFoundError:
    print("NOFILE")
except PermissionError:
    print("NOPERM")
            