def f(n):
    if n <= 1:
        return 1
    return n *f(n - 1)
def ds(x):
    if x < 10:
        return x 
    return x % 10 + ds(x // 10)
print(ds(f(int(input()))))