class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for _ in range(target)] for _ in range(n)]
        for i in range(target):
            dp[0][i] = 1 if i < k else 0
        for i in range(1, n):
            for j in range(target):
                s = max(0, j-k)
                dp[i][j] = sum(dp[i-1][s:j]) % (10**9 + 7)
        return dp[-1][-1] % (10**9+7) 