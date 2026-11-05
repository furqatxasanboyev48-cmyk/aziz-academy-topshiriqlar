nums = input().split()
def rl(a):
    if not a:
        return []
    return rl(a[1:]) + [a[0]]
print(' '.join(rl(nums)))