class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        s=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count = self.dfs(grid, i, j, 1)
                    s = max(s, count)
        return s
        
    def dfs(self, grid, x, y, count):
        test = [(x,y-1), (x,y+1), (x-1,y), (x+1,y)]
        final = []
        for t in test:
            if t[0]>=0 and t[1]>=0 and t[0]<len(grid) and t[1]<len(grid[0]):
                final.append(t)
        grid[x][y]=0
        for f in final:
            if grid[f[0]][f[1]]==1:
                count+=1
                count = self.dfs(grid, f[0], f[1], count)
        return count