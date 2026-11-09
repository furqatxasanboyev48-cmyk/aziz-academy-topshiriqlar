def do_a(x):
    return x + 1
def do_b(x):
    return x * 2
a_mod = {"do": do_a}
b_mod = {"do": do_b}
x = int(input())
print(a_mod["do"](x))
print(b_mod["do"](x))