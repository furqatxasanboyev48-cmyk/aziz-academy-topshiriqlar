def ssum(nums):
    return sum(nums)
def mean(nums):
    return sum(nums) / len(nums)
stats = {"sum": ssum, "mean": mean}
nums = list(map(int, input().split()))
print(stats["sum"](nums))
print(f"{stats['mean'](nums):.2f}")