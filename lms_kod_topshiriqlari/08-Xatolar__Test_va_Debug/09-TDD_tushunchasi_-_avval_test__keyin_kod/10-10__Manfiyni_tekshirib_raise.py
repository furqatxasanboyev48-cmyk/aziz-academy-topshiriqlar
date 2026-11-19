def tekshir(n):
    if n < 0:
        raise ValueError("manfiy")
    return n 
n = int(input())
try:
    print(tekshir(n))
except ValueError:
    print("Xato: manfiy son")