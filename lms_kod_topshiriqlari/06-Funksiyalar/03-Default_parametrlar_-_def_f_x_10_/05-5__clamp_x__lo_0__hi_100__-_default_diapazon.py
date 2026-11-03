def clamp(x, lo=0, hi=100):
    if x < lo:
        return lo 
    if x > hi:
        return hi
    return x
sonlar = [int(t) for t in input().split()]
if len(sonlar) == 1:
    print(clamp(sonlar[0]))
elif len(sonlar) == 2:
    print(clamp(sonlar[0], sonlar[1]))
else:
    print(clamp(sonlar[0], sonlar[1], sonlar[2]))