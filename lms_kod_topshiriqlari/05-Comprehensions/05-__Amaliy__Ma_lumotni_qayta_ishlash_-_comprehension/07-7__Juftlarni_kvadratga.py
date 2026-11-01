sonlar = [int(x) for x in input().split()]
print([x * x for x in sonlar if x % 2 == 0])