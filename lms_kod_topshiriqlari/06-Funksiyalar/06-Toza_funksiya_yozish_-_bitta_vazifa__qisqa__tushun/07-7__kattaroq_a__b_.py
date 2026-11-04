def kattaroq(a, b):
    return a if a > b else b 
a, b = map(int, input().split())
print(kattaroq(a, b))