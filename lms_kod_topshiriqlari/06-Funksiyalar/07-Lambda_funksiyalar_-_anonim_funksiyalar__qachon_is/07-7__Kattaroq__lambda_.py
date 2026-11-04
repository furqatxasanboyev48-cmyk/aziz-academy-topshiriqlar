kattaroq = lambda a, b: a if a > b else b 
a, b = map(int, input().split())
print(kattaroq(a, b))