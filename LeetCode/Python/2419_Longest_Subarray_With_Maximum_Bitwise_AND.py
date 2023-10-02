class Solution:
    # This question is basically asking: find the longest subarray that consists only of the maximum element
    # m = max(nums)
    # curr = 0
    # best = 0
    # for num in nums:
    #     if num == m:
    #         curr += 1
    #     else:
    #         curr = 0
    #     best = max(curr, best)
    # return best
    def longestSubarray(self, nums: List[int]) -> int:
        high = 0
        curr = 0
        best = 0
        for num in nums:
            if num == high:
                curr += 1
                best = max(best, curr)
            elif num > high:
                high = num
                curr = 1
                best = 1
            else:
                curr = 0
        return best