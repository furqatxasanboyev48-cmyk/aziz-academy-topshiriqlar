def parse_ints(line):
    return [int(x) for x in line.split()]
def mean(nums):
    return sum(nums) / len(nums)
def minmax(nums):
    return (min(nums), max(nums))
def count_pos_neg(nums):
    pos = 0
    neg = 0
    for x in nums:
        if x > 0:
            pos += 1 
        elif x < 0:
            neg += 1 
    return (pos, neg)
def report(nums):
    n = len(nums)
    m = mean(nums)
    mn, mx = minmax(nums)
    p, g = count_pos_neg(nums)
    return f"count={n} mean={m:.2f} min={mn} max={mx} pos={p} neg={g}"
nums = parse_ints(input())
print(report(nums))
