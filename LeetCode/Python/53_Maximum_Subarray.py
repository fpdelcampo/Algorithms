class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_best=-10**6
        total_best=-10**6
        for i in nums:
            current_best = max(i, current_best+i)
            total_best = max(current_best, total_best)
        return total_best
    