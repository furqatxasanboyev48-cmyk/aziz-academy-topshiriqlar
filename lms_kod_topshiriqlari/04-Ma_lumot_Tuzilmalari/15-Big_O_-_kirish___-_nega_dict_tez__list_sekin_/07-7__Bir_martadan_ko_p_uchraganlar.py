nums = input().split()
cnt = {}
for x in nums:
    cnt[x] = cnt.get(x, 0) + 1
res = sum(1 for v in cnt.values() if v > 1)
print(res)