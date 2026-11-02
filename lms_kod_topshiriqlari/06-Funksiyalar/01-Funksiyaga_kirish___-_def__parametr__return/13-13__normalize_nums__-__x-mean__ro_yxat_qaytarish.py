def normalize(nums):
    mean = sum(nums) / len(nums)
    return [ x - mean for x in nums]
nums = [int(t) for t in input().split()]
natija = normalize(nums)
print(" ".join (f"{x:.2f}" for x in natija))
