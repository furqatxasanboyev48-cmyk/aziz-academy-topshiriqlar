def add(a, b):
    return a + b 
def sub(a, b):
    return a - b 
ops = {"add": add, "sub": sub} 
a, b = map(int, input().split())
print(ops["add"](a, b))
print(ops["sub"](a, b))
