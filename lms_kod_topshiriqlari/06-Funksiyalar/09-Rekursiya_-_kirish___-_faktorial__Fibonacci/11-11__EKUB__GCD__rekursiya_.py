def g(a, b):
    if b == 0:
        return a 
    return g(b, a % b)
a, b = map(int, input().split())
print(g(a, b))