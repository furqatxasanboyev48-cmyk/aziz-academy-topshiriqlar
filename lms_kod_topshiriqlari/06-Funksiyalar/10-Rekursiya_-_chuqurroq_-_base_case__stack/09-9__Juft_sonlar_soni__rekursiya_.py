nums = list(map(int, input().split()))
def ce(a):
    if not a:
        return 0
    return (1 if a[0] % 2 == 0 else 0) + ce(a[1:])
print(ce(nums))