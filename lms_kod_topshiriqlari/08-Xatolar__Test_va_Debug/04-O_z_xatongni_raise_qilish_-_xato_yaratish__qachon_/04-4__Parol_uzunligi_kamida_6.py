password = input()
try:
    if len(password) < 6:
        raise ValueError("qisqa")
except ValueError:
    print("WEAK")
else:
    print("OK")
        