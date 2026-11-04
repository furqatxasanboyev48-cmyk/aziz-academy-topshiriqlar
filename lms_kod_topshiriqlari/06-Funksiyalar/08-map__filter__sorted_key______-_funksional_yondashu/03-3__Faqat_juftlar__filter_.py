nums = list(map(int, input().split()))
print(' '.join(map(str, filter(lambda x: x % 2 == 0, nums))))