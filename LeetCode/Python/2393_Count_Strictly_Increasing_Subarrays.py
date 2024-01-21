class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        last = nums[0]
        count = 1
        res = 1
        for num in nums[1:]:
            if num > last:
                count += 1
            else:
                count = 1
            res += count
            last = num
        return res