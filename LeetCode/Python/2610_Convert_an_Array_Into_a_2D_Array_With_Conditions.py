class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        count = [0]*n
        m = 0
        for i in range(n):
            count[nums[i]-1] += 1
            m = max(m, count[nums[i]-1])
        res = []
        for i in range(m):
            row = []
            for j in range(n):
                if count[j] - 1 >= i:
                    row.append(j+1)
            res.append(row)
        return res