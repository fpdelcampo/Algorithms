class Solution:
    # Read up on cycle sort
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums):
            if nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(nums[i])
        return res