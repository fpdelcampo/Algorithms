class Solution:
    #1, 4, 6, 7 ...
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        res = 0
        n = len(nums)
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                idx = stack.pop()
                res += i - idx
            stack.append(i)
        while stack:
            idx = stack.pop()
            res += n - idx
        return res