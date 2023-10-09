class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        m = 0
        for num in arr:
            if -10000 <= num - difference <= 10000 and num - difference in dp:
                dp[num] = 1+dp[num - difference]
            if num not in dp:
                dp[num] = 1
            m = max(m, dp[num])
        return m