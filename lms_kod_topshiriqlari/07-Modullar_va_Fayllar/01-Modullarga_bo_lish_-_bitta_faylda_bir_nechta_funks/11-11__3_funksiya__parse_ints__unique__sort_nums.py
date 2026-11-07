def parse_ints(line):
    return [int(x) for x in line.split()]
def unique(nums):
    return list(set(nums))
def sort_nums(nums):
    return sorted(nums)
nums = sort_nums(unique(parse_ints(input())))
print(" ".join(str(x) for x in nums))