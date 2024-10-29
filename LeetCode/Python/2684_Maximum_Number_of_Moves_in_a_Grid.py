class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        res = 0
        for j in range(cols):
            for i in range(rows):
                match = False
                if j + 1 < cols:
                    if i - 1 >= 0 and grid[i][j] < grid[i - 1][j + 1] and (j == 0 or dp[i][j] > 0):
                        dp[i - 1][j + 1] = max(dp[i - 1][j + 1], 1 + dp[i][j])
                        res = max(res, dp[i - 1][j + 1])
                
                    if i + 1 < rows and grid[i][j] < grid[i + 1][j + 1] and (j == 0 or dp[i][j] > 0):
                        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], 1 + dp[i][j])
                        res = max(res, dp[i + 1][j + 1])

                    if grid[i][j] < grid[i][j + 1] and (j == 0 or dp[i][j] > 0):
                        dp[i][j + 1] = max(dp[i][j + 1], 1 + dp[i][j])
                        res = max(res, dp[i][j + 1])
        return res 