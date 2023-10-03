class Solution:
    # This problem is just asking us to find the maximum in log time
    # The trick is that the array has a special quasi-sortedness which we can exploit
    # We can use binary search somehow
    # Basically if nums[m] > nums[r], then we know that the mountain is to the right of or at m
    # Similarly if nums[m] < nums[l], then we know the mountain is to the left of or at m
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while l <= r:
            m = (l+r) // 2
            if arr[m-1] < arr[m] > arr[m+1]:
                return m
            if arr[m] > arr[m+1]:
                r = m-1
            else:
                l = m+1
        return -1