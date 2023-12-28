class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        n = len(nums1)
        return sum([nums1[i]*nums2[n-i-1] for i in range(n)])