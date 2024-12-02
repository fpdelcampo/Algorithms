class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        MOD = 10 ** 9 + 7
        for i in range(len(nums)): # just need to locate target - nums[i]
            idx = bisect_right(nums, target - nums[i])
            if idx > i:
                res += (2 ** (idx - i - 1))
                res %= MOD
        return res