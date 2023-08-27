class Solution:
    # We have a rotated array
    # There is a "flip" at one index in the array (where a[i] > a[i+1])
    # In one half of the array, the left is less than the right.
    #       If we are in this half,  binary search behaves as normal
    # In the other half of the array, the left is greater than the right
    #       If we are in this half, binary search is doe snot behave as normal

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                return middle
            # This checks if the left half is sorted
            if nums[left] <= nums[middle]:
                # If the target is in the sorted portion
                if nums[left] <= target <= nums[middle]:
                    right = middle-1
                # Otherwise, the target is not in the sorted portion
                else:
                    left = middle+1
            # This checks if the right half is sorted
            else:
                # If the target is in the sorted half
                if nums[middle] <= target <= nums[right]:
                    left = middle+1
                else:
                    right = middle-1     
        return -1