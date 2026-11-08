def mean(nums):
    return sum(nums) / len(nums)
def median(nums):
    tartib = sorted(nums)
    n = len(tartib)
    if n % 2 == 1:
        return tartib[n // 2]
    return (tartib[n // 2 - 1] + tartib[n // 2]) / 2
nums = list(map(int, input().split()))
print(f"{mean(nums):.2f}")
print(f"{median(nums):.2f}")