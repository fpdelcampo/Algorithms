class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swapped = 0
        start = 0
        n = len(nums)
        k %= n
        if k != 0:
            while swapped < n:
                init = start
                element = nums[init]
                while True:
                    next = (init+k) % n
                    nums[next], element = element, nums[next]
                    init = next
                    swapped += 1
                    if init == start:
                        break
                start += 1
                n = len(nums)
        k %= n