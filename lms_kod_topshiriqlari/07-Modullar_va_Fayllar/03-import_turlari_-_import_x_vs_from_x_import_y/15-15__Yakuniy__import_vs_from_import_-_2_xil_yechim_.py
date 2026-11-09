def inc(x):
    return x + 1
def dec(x):
    return x - 1
ops = {"inc": inc, "dec": dec}
x = int(input())
cmd = input().strip()
print(ops[cmd](x))
fn = ops[cmd]
print(fn(x))