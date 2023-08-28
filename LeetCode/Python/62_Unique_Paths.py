class Solution:
    def factorial(n):
        if n in [0,1]:
            return 1
        return n*factorial(n-1)

    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(n+m-2)/(factorial(n-1)*factorial(m-1)))

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if m == 1 or n == 1:
            return 1
        dp[1][0] = 1
        dp[0][1] = 1
        for i in range(m):
            for j in range(n):
                if (i, j) in [(0,0), (1,0), (0,1)]:
                    continue
                vals = []
                if 0 <= i-1 < m:
                    vals.append(dp[i-1][j])
                if 0 <= j-1 < n:
                    vals.append(dp[i][j-1])
                dp[i][j] = sum(vals)
        return dp[m-1][n-1]