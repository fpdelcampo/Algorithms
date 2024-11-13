# This would be easy if I had two arrays that said "you have x entries in num greater/less than y"
# Can do something similar with binary search, but just need to be careful about edge cases
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            lb = bisect_left(nums, lower - nums[i], i + 1)
            ub = bisect_right(nums, upper - nums[i], i + 1)
            res += ub - lb
        return res