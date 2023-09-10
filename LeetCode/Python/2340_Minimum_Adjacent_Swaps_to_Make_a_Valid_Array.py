class Solution:
    # Here the idea is simple
    # We first find the the left-most index of the smallest element and the right-most index of the largest element, which we will call l and r
    # If l<r, then swapping the smallest number to get it to the first location will never affect the largest element
    # Therefore, the number of swaps we need to get the smallest number into the right location is l
    # Similarly, if the array has length 5 and r = 3, we need to perform 5-3+1 = 1 swap
    # Now if l>r, we will do one left swap since we will most the left and right in the proper direction on one of the swaps
    def minimumSwaps(self, nums: List[int]) -> int:
        smallest = float('inf')
        largest = float('-inf')
        n = len(nums)-1
        l = 0
        r = n-1
        for i in range(len(nums)):
            if nums[i] < smallest:
                smallest = nums[i]
                l = i
            if nums[i] >= largest:
                largest = nums[i]
                r = i
        if l>r:
            return l+(n-r)-1
        else:
            return l+(n-r)