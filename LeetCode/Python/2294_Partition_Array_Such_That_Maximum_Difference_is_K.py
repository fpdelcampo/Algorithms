class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr_min = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] - curr_min > k:
                curr_min = nums[i]
                count +=1 
        return count