class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for num in nums[1:]:
            prefix.append(num + prefix[-1])
        res = []
        n = len(nums)
        for i in range(n):
            left = 0
            right = 0
            if i > 0:
                left = -prefix[i] + (i+1)*nums[i]
            if i < len(nums) - 1:
                right = prefix[-1] - prefix[i] - (n - i - 1)*nums[i]
            res.append(left+right)
        return res