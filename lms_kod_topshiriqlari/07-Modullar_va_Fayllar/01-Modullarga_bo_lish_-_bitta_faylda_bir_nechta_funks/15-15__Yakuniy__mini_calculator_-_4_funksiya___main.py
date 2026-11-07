def add(a, b):
    return a + b 
def sub(a, b):
    return a - b 
def mul(a, b):
    return a * b 
def div(a, b):
    if b == 0:
        return None
    return a / b 
def calc(op, a, b):
    if op == "add":
        return add(a, b)
    if op == "sub":
        return sub(a, b)
    if op == "mul":
        return mul(a, b)
    return div(a, b)
q = int(input())
for _ in range(q):
    op, a, b = input().split()
    a = int(a)
    b = int(b)
    natija = calc(op, a, b)
    if op == "div":
        if natija is None:
            print("ERROR")
        else:
            print(f"{natija:.2f}")
    else:
        print(natija)
    
   