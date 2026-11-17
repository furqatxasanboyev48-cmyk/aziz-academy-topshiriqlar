filename = input().strip()
try:
    if not filename.endswith(".txt"):
        raise ValueError("txt emas")
except ValueError:
    print("BAD")
else:
    print("OK")
        