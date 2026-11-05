nums = list(map(int, input().split()))
def mx(a):
    if len(a) == 1:
        return a[0]
    m = mx(a[1:])
    return a[0] if a[0] > m else m 
print(mx(nums))