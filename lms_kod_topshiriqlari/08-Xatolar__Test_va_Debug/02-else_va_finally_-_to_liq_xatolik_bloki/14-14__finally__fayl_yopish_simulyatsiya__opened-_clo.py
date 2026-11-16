mode = input().strip()
opened = True
closed = False
try:
    if mode == "0":
        1/0
except ZeroDivisionError:
        pass
finally:
    opened = False
    closed = True
print("YES" if (not opened and closed) else "NO")
        