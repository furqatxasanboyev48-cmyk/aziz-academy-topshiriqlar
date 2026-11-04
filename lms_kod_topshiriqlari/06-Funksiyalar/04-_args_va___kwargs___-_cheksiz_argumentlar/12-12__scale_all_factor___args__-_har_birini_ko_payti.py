def scale_all(factor, * args):
    return [factor * x for x in args]
factor = int(input())
nums = [int(t) for t in input().split()]
natija = scale_all(factor, *nums)
print(" ".join(str(x) for x in natija))