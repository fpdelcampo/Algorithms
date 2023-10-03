class Solution:
    # We need to use binary search somehow
    # Thus, we need to be able to have something to the effect of:
    # if condition: search left
    # else: search right
    # So basically, how can we know that the peak is in the left half vs right half
    # We know there is a peak in the left half if: 
    def findPeakElement(self, nums: List[int]) -> int:
        # First we handle edge cases
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[m-1] < nums[m] > nums[m+1]:
                return m
            prev = float('-inf') if m == 0 else nums[m-1] # handles the edge case where m = 0
            if prev < nums[m]:
                l = m+1
            else:
                r = m-1
            print(l, m, r)

        return m