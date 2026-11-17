n = int(input())
try:
    if n % 2 != 0:
        raise ValueError("toq")
except ValueError:
    print("ODD")
else:
    print("EVEN")
        
    