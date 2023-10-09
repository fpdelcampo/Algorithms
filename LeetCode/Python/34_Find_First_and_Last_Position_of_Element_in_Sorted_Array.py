class Solution:
    # We need to do binary search somehow
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        l = 0
        r = len(nums)-1
        left = -1
        right = -1
        m = 0
        # Look for left-most occurrence
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                left = m
            if  nums[m] < target:
                l = m+1
            else:
                r = m-1
        l = 0
        r = len(nums)-1
        # Look for right-most occurrence
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                right = m
            if nums[m] <= target:
                l = m+1
            else:
                r = m-1
        return [left, right]
        
