s = input()
closed = False
try:
    int(s)
except ValueError:
    pass
finally:
    closed = True
print("YES" if closed else "NO")