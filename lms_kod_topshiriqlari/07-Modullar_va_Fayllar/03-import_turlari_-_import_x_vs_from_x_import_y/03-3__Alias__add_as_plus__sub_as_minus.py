def add(a, b):
    return a + b 
def sub(a, b):
    return a - b 
plus = add 
minus = sub
a, b = map(int, input().split())
print(plus(a, b))
print(minus(a, b))
