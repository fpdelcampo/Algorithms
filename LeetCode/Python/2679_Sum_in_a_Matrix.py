class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        rows = len(nums)
        cols = len(nums[0])
        for i in range(rows):
            nums[i].sort()
        res = 0
        for j in range(cols):
            m = 0
            for i in range(rows):
                m = max(m, nums[i][j])
            res += m
        return res