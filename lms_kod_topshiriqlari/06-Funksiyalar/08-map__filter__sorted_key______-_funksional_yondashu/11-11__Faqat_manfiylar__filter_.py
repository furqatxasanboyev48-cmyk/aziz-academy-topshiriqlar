nums = list(map(int, input().split()))
print(' '.join(map(str, filter(lambda x: x < 0, nums))))