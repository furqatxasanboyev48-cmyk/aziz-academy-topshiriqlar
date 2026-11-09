def inc(x):
    return x + 1 
mod = {"inc": inc}
x = int(input())
print(mod["inc"](x))
inc_func = mod["inc"]
print(inc_func(x))
