def min_all(*args):
    return min(args)
nums = [int(t) for t in input().split()]
print(min_all(*nums))