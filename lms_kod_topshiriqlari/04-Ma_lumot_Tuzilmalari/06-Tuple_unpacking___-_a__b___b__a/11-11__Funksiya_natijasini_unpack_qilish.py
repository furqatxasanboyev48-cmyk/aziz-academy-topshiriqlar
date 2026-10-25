def hisobla(a, b):
    return a + b, a * b
a, b = map(int, input().split())
yigindi, kopaytma = hisobla(a, b)
print(yigindi)
print(kopaytma)