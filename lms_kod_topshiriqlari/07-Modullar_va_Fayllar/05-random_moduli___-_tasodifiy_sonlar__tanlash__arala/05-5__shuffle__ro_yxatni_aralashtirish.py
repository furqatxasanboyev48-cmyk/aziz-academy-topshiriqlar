import random
seed = int(input())
nums = input().split()
random.seed(seed)
random.shuffle(nums)
print(" ".join(nums))