class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # You can connect the element from grid[i][j] to any element from grid[i+1] except grid[i+1][j]. For that testcase: -46-7-76+10-73 = -192
        n = len(grid)
        if n == 1:
            return grid[0][0]
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        dp[0] = grid[0]
        for i in range(1, n):
            min1 = float('inf')
            min2 = float('inf')
            idx1 = 0
            idx2 = 0
            for j in range(n):
                if dp[i-1][j] < min1:
                    min2 = min1
                    idx2 = idx1
                    min1 = dp[i-1][j]
                    idx1 = j
                elif dp[i-1][j] < min2:
                    min2 = dp[i-1][j]
                    idx2 = j
            for j in range(n):
                if j == idx1:
                    dp[i][j] = min(dp[i][j], min2 + grid[i][j])
                else:
                    dp[i][j] = min(dp[i][j], min1 + grid[i][j])
        return min(dp[-1])