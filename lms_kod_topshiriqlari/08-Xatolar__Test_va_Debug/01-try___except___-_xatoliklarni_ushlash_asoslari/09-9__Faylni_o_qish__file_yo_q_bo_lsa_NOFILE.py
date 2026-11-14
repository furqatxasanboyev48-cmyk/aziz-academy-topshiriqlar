import os
mode = input().strip()
text = input().strip()
if os.path.exists("ex9.txt"):
    os.remove("ex9.txt")
if mode == "1":
    with open("ex9.txt", "w") as f:
        f.write(text)
try:
    with open("ex9.txt") as f:
        print(f.read())
except FileNotFoundError:
        print("NOFILE")