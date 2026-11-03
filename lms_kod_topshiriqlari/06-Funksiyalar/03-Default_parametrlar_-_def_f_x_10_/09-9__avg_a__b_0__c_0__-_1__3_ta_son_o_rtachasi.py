def avg(a,b=None, c=None):
    if b is None:
        return a / 1
    if c is None:
        return(a + b) / 2
    return(a + b + c) / 3
sonlar = [int(t) for t in input().split()]
if len(sonlar) == 1:
    natija = avg(sonlar[0])
elif len(sonlar) == 2:
    natija = avg(sonlar[0], sonlar[1])
else:
    natija = avg(sonlar[0], sonlar[1], sonlar[2])
print(f"{natija:.2f}")