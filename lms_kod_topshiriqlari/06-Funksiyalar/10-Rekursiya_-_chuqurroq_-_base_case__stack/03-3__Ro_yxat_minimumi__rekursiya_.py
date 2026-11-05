nums = list(map(int, input().split()))
def mn(a):
    if len(a) == 1:
        return a[0]
    m = mn(a[1:])
    return a[0] if a[0] < m else m 
print(mn(nums))