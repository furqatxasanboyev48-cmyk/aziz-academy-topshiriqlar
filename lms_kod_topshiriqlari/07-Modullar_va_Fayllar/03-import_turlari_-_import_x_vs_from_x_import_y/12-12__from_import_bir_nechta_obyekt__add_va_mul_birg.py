def add(a, b):
    return a + b 
def mul(a, b):
    return a * b 
ops = {"add": add, "mul": mul}
add_fn = ops["add"]
mul_fn = ops["mul"]
a, b = map(int, input().split())
mode = input().strip()
if mode == "add":
    print(add_fn(a, b))
else:
    print(mul_fn(a, b))