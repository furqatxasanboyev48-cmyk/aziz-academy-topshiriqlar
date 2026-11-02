def min_max(nums):
    return(min(nums), max(nums))
nums = [int(t) for t in input().split()]
mn, mx = min_max(nums)
print(mn)
print(mx)