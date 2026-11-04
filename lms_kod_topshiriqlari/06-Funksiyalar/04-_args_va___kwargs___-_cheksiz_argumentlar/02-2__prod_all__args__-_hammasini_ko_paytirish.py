def prod_all(*args):
    natija = 1
    for x in args:
        natija *= x
    return natija
nums = [int(t) for t in input().split()]
print(prod_all(*nums))