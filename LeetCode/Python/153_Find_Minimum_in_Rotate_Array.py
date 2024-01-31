class Solution:
    # Idea is that there are "two sorted arrays"
    # Basically, a[i] < a[i+1] for all but one i, and we want to find that i to return a[i]
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        if nums[0] > nums[1]:
            return nums[1]
        if nums[-1] < nums[-2]:
            return nums[-1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > nums[middle + 1]:
                return nums[middle+1]
            if nums[middle-1] > nums[middle]:
                return nums[middle]
            if nums[middle] > nums[0]:
                left = middle + 1
            else:
                right = middle - 1
        return -1