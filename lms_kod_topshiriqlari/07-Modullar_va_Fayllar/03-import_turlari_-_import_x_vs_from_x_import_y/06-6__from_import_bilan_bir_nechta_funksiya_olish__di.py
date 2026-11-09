def min2(a, b):
    if a < b:
        return a 
    return b 
def max2(a, b):
    if a > b:
        return a 
    return b 
ops = {"min2": min2, "max2": max2}
min_fn = ops["min2"]
max_fn = ops["max2"]
a, b = map(int, input().split())
print(min_fn(a, b))
print(max_fn(a, b))