s = input()
try:
    if not s.strip():
        raise ValueError("bo'sh")
except ValueError:
    print("EMPTY")
else:
    print("OK")