def unique(nums):
    return list(set(nums))
def sorted_unique(nums):
    return sorted(unique(nums))
nums = list(map(int, input().split()))
natija = sorted_unique(nums)
print(" ".join(str(x) for x in natija))