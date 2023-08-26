class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        small = 1
        large = 1
        best = max(nums)
        for num in nums:
            if num == 0:
                small = 1
                large = 1
            else:
                c = small
                small = min(small*num, large*num, num)
                large = max(c*num, large*num, num)
                best = max(best, small, large)
        return best