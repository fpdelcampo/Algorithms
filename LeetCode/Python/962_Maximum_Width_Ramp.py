# This question is basically asking, find the furthest apart pair i,j such that i < j and nums[i] <= nums[j]
# From the time constraints, we should aim for O(nlogn) or O(n)
# There is monotonicity to the problem.  If we have that nums[j] > nums[j + k] for example, then any pair involving i and j could use i and j + k instead.
# The goal should be to have a decreasing stack a_m, ... a_n where each entry is an index, and the sequence nums[a_n], ... nums[a_m] is strictly decreasing
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                idx = stack.pop()
                res = max(res, j - idx)
        return res           