# Key idea is that it is optimal to jump to the nearest index with greater value
# Proof, suppose i < j, a[j] > a[i], then for any k, score of going from i to j to k is (j - i) * nums[i] + (k - j) * nums[j], while score of going directly to k is (k - i) * nums[i].  The first expression is clearly larger

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        last = 0
        score = 0
        for i in range(1, len(nums)):
            if nums[last] < nums[i]:
                score += (i - last) * nums[last]
                last = i
        return max(score + (len(nums) - 1 - last) * nums[last], (len(nums) - 1) * nums[0])