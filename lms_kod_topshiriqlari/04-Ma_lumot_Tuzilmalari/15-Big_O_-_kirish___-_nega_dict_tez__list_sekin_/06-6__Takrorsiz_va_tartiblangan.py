nums = [int(x) for x in input().split()]
u = sorted(set(nums))
print(" ".join(str(x) for x in u))