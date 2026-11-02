def div(a, b):
    if b == 0:
        return "ERROR"
    return a / b 
qator = input().split()
a = int(qator[0])
b = int(qator[1])
natija = div(a, b)
if natija == "ERROR":
    print("ERROR")
else:
    print(f"{natija:.2f}")
        
    