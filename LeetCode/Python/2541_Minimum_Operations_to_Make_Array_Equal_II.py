class Solution:
    # When can we not make nums1 == nums2? If the absolute difference for any pair is not divisible by k, and if the number of times we have to add k is not equal to the number of times we need to subtract k
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1
        add = 0
        sub = 0
        for i in range(len(nums1)):
            if abs(nums1[i] - nums2[i]) % k != 0:
                return -1
            elif nums1[i] > nums2[i]:
                add += (nums1[i] - nums2[i]) // k
            else:
                sub += (nums2[i] - nums1[i]) // k
        if add != sub:
            return -1
        else:
            return add