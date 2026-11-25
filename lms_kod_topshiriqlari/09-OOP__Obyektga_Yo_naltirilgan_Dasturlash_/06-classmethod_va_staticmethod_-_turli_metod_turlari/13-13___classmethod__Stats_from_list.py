class Stats:
    def __init__(self, avg):
        self.avg = avg
    @classmethod
    def from_list(cls, nums):
        return cls(sum(nums) // len(nums))
nums = list(map(int, input().split()))
print(Stats.from_list(nums).avg)