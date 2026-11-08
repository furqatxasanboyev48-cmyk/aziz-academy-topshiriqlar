def add(a, b):
    return a + b 
def mul(a, b):
    return a * b 
def pow(a, b):
    return a ** b 
def dispatch(cmd, * args):
    if cmd == "add":
        return add(*args)
    if cmd == "mul":
        return mul(*args)
    return pow(*args)
q = int(input())
for _ in range(q):
    cmd, a , b = input().split()
    print(dispatch(cmd, int(a), int(b)))