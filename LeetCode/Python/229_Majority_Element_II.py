class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return list(set(nums))
        nums.sort()
        res = set()
        n = len(nums)
        i = 1
        j = 1
        while i < n:
            if nums[i] == nums[i-1]:
                j += 1
            else:
                j = 1
            if j > n // 3:
                res.add(nums[i])
            i += 1
        return list(res)
