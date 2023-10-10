class Solution:
    # So let's say we know the longest non-dec subarray from two arrays up to index i
    # Then we can use DP
    # DP[i+1] = max(DP[j] for all j<i+1 and the element at j is less than the element at i+1)    
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        dp1 = [1 for _ in range(l1)]
        dp2 = [1 for _ in range(l1)]
        m = 1
        for i in range(1, l1):
            tmp1 = 0
            tmp2 = 0
            tmp3 = 0
            tmp4 = 0
            if nums1[i] >= nums1[i-1]:
                tmp1 = 1+dp1[i-1]
            if nums1[i] >= nums2[i-1]:
                tmp2 = 1+dp2[i-1]
            if nums2[i] >= nums1[i-1]:
                tmp3 = 1+dp1[i-1]
            if nums2[i] >= nums2[i-1]:
                tmp4 = 1+dp2[i-1]
            dp1[i] = max(dp1[i], tmp1, tmp2)
            dp2[i] = max(dp2[i], tmp3, tmp4)
            m = max(m, dp1[i], dp2[i])      
        return m