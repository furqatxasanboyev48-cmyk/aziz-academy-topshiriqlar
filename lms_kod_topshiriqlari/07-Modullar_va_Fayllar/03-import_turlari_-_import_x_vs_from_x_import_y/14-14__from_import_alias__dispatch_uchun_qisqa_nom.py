def add(a, b):
    return a + b 
def sub(a, b):
    return a - b 
def mul(a, b):
    return a * b 
ops = {"add": add, "sub": sub, "mul":mul}
disp = ops
q = int(input())
for _ in range(q):
    op, a, b = input().split()
    print(disp[op](int(a), int(b)))
