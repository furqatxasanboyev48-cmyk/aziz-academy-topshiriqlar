def power(a, b):
    return a ** b 
ops = {"power": power}
p = ops["power"]
pow_fn = p 
a, b = map(int, input().split())
print(pow_fn(a, b))