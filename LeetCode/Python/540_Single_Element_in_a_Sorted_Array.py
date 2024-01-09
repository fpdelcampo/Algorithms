class Solution:
    # Idea is to do a binary search.  First check the middle element by comparing to its neighbors. If no match, return the middle.
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # handle edge cases
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            left = nums[m-1] == nums[m]
            right = nums[m] == nums[m+1]
            if not left and not right:
                return nums[m]
            if left:
                if (m - l) % 2 == 1:
                    l = m + 1
                else:
                    r = m - 2
            else:
                if (m - l) % 2 == 0:
                    l = m + 2
                else:   
                    r = m - 1
        return nums[m]