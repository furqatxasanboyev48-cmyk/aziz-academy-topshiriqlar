def sum_all(*args):
    return sum(args)
nums = [int(t) for t in input().split()]
print(sum_all(*nums))