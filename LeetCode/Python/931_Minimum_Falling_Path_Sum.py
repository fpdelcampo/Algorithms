class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        dp[0] = matrix[0]
        for i in range(1, n):
            for j in range(n):
                points = [[i - 1, j]]
                if j > 0:
                    points.append([i - 1, j - 1])
                if j < n - 1:
                    points.append([i - 1, j + 1])
                for point in points:
                    dp[i][j] = min(dp[i][j], dp[point[0]][point[1]])
                dp[i][j] += matrix[i][j]
        return min(dp[-1])