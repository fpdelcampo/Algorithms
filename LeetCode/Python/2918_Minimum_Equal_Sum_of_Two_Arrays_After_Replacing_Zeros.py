class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        s1 = 0
        s2 = 0
        z1 = 0
        z2 = 0
        for i in range(max(m, n)):
            if i < m:
                if nums1[i] == 0:
                    z1 += 1
                s1 += nums1[i]
            if i < n:
                if nums2[i] == 0:
                    z2 += 1 
                s2 += nums2[i]

        # Check if it's impossible

        if s1 == s2 and ((z1 > 0 and z2 == 0) or (z2 > 0 and z1 == 0)):
            return -1
        
        if s1 > s2:
            if z2 == 0:
                return -1
            if z1 == 0 and z2 > (s1 - s2):
                return -1

        if s2 > s1:
            if z1 == 0:
                return -1
            if z2 == 0 and z1 > (s2 - s1):
                return -1
        
        return max(s1 + z1, s2 + z2)