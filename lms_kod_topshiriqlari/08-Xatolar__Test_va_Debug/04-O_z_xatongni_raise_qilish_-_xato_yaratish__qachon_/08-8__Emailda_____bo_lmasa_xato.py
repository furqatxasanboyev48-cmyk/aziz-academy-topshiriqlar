email = input().strip()
try:
    if '@' not in email:
        raise ValueError("email xato")
except ValueError:          
    print("BAD")
else:
    print("OK")