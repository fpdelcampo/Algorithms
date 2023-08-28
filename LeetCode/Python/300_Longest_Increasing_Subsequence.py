class Solution:
    # Suppose DP[i] represents the longest subsequence up to index i
    # Then we want to find some way to get DP[i+1]
    # The trick is to iterate through all DP[j] for j<i+1.  If nums[j] < nums[i+1], DP[i+1] = max(1+DP[j], DP[i+1])

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i+1):
                if nums[j] < nums[i]:
                    dp[i] = max(1+dp[j], dp[i])
        return max(dp)