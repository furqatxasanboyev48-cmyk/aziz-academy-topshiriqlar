n = int(input())
try:
    if n <= 0:
        raise ValueError("musbat emas")
except ValueError:
    print("ERROR")
else:
    print("OK")
        