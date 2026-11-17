n = int(input())
try:
    if n < 10:
        raise ValueError("kichik")
except ValueError:
    print("SMALL")
else:
    print("OK")
    