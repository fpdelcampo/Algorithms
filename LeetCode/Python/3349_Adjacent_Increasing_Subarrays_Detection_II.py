class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev = 0
        curr = 1
        res = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr += 1
            else:
                res = max(res, min(prev, curr), curr // 2)
                prev = curr
                curr = 1
        res = max(res, min(prev, curr), curr // 2)
        return res