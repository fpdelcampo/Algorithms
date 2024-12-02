# Need to track a subarray in which a deletion has been made, a subarray in which no such deletion has been made, and a best answer
# Probably can do this in constant space

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        best, curr, deletion = 0, 0, 0
        zero = False
        for i in range(len(nums)):
            if nums[i] == 1:
                if deletion > 0:
                    deletion += 1
                curr += 1
            else:
                zero = True
                deletion = curr
                curr = 0
            best = max(best, curr, deletion)
        return max(best, curr, deletion) if zero else len(nums) - 1