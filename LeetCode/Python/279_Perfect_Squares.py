# The article shares a bunch of awesome approaches
# https://leetcode.com/problems/perfect-squares/description/

class Solution:
    # Let dp[i-1] store the answer for the least number of perfect squares that sum to i
    def numSquares(self, n: int) -> int:
        sqs = [i**2 for i in range(1, 1+int(n**0.5))]
        dp = [10001 for _ in range(n+1)]
        for sq in sqs:
            dp[sq] = 1
        for i in range(1, n+1):
            for j in sqs:
                if i < j:
                    break
                dp[i] = min(dp[i], 1+dp[i-j])
        return dp[-1]