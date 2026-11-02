def stats(nums):
    return {'count': len(nums), 'sum': sum(nums), 'min': min(nums), 'max': max(nums)}
nums = [int(t) for t in input().split()]
print(stats(nums))
