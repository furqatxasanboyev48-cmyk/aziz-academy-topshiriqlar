def avg_all(*args):
    return sum(args) / len(args)
nums = [int(t) for t in input().split()]
print(f"{avg_all(*nums):.2f}")