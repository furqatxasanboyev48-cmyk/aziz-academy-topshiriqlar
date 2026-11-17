op = input().strip()
try:
    if op not in ("ADD", "SUB"):
        raise ValueError("operator xato")
except ValueError:  
    print("OPERR")
else:
    print("OK")