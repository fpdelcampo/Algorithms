class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_zero = 0
        for idx, num in enumerate(nums):
            if num != 0:
                nums[last_zero], nums[idx] = nums[idx], nums[last_zero]
                last_zero += 1
