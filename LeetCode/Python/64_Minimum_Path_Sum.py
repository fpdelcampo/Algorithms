class Solution:
    # We want to use dynamic programming
    # We note that MPS(i, j) = grid[i][j] + min(MPS(i-1, j), MPS(i, j-1))
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[rows-1][cols-1] = grid[rows-1][cols-1]
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if i == rows-1 and j == cols-1:
                    continue
                to_check = []
                if i < rows - 1:
                    to_check.append(dp[i+1][j])
                if j < cols - 1:
                    to_check.append(dp[i][j+1])
                dp[i][j] = grid[i][j] + min(to_check)
        return dp[0][0]