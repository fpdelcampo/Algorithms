class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        evens = 0
        odds = 0
        one = 1
        if nums[0] % 2:
            odds += 1
        else:
            evens += 1
        parity = (nums[0] % 2) ^ 1
        for i in range(1, len(nums)):
            if nums[i] % 2 == parity:
                one += 1
                parity ^= 1
            if nums[i] % 2 == 0:
                evens += 1
            else:
                odds += 1

        return max(one, evens, odds)