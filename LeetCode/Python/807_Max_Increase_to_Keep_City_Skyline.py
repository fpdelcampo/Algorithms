class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row = [0 for _ in range(n)]
        col = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                row[i] = max(row[i], grid[i][j])
                col[j] = max(col[j], grid[i][j])
        res = 0
        for i in range(n):
            for j in range(n):
                res += min(row[i], col[j]) - grid[i][j]
        return res