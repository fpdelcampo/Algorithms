class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = {}
        cols = {}
        x = len(grid)
        y = len(grid[0])
        for i in range(x):
            for j in range(y):
                if grid[i][j]:
                    if i in rows:
                        rows[i] += 1
                    else:
                        rows[i] = 1
                    if j in cols:
                        cols[j] += 1
                    else:
                        cols[j] = 1
        for i in range(x):
            if i not in rows:
                rows[i] = 0
        for j in range(y):
            if j not in cols:
                cols[j] = 0
        ret = [[-x - y + 2*rows[i] + 2*cols[j] for j in range(y)] for i in range(x)]
        return ret