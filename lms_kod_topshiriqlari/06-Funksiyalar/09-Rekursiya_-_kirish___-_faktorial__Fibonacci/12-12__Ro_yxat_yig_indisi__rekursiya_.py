nums = list(map(int, input().split()))
def ls(a):
    if not a:
        return 0
    return a[0] + ls(a[1:])
print(ls(nums))