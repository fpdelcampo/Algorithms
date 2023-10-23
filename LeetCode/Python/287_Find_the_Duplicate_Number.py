class Solution:
    # Apparently there is an O(n) solution based on Floyd's algorithm
    def findDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        ans = -1
        while l <= r:
            m = (l+r)//2
            count = 0
            for num in nums:
                if num <= m:
                    count += 1
            if count > m:
                ans = m
                r = m-1
            else:
                l = m+1
        return ans