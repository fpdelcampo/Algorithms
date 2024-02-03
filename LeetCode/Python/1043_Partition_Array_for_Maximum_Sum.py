class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0 for i in range(len(arr) + 1)]
        for i in range(len(arr) - 1, -1, -1):
            curr = 0 
            for j in range(i, min(len(arr), i + k)):
                curr = max(curr, arr[j])
                dp[i] = max(dp[i], dp[j + 1] + curr * (j - i + 1))
        return dp[0]