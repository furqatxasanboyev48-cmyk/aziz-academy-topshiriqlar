def add(a, b):
    return a + b 
def mul(a, b):
    return a * b 
ops = {"add": add, "mul": mul}
add_func = ops["add"]
mul_func = ops["mul"]
a, b = map(int, input().split())
print(add_func(a, b))
print(mul_func(a, b))

