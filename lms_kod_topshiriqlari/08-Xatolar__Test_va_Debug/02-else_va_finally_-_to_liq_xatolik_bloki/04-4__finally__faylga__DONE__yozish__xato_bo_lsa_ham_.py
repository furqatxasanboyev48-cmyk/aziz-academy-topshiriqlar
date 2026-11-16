mode = input().strip()
text = input().strip()
f = open("ex4.txt", "w")
try:
    if mode == "1":
        f.write(text)
    else:
        1/0
except ZeroDivisionError:
    pass
finally:
    f.write("\nDONE")
    f.close()
with open("ex4.txt") as f:
    lines = f.read().strip().split("\n")
print(lines[-1])
    