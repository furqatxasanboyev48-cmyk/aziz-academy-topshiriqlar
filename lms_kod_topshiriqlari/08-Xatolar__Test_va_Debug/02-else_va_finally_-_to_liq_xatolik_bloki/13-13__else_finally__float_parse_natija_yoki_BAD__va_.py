s = input()
try:
    float(s)
except ValueError:
    out = "BAD"
else:
    out = "OK"
finally:
    out += "."
print(out)