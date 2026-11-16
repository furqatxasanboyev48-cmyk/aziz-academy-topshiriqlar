mode = input().strip()
out = ""
try:
    if mode == "1":
        out = "OK"
    else:
        1/0
except ZeroDivisionError:
    out = "ERR"
finally:
    out = out + " CLEAN"
print(out)
        