def max_all(*args):
    return max(args)
nums = [int(t) for t in input().split()]
print(max_all(*nums))