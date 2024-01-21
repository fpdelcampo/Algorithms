class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # For each node, try to do a dfs and see if you reach every node
        
        mat = [[0 for _ in range(n)] for _ in range(n)]
        for edge in edges:
            x, y = edge
            mat[x][y] = 1
        
        def dfs(node, visited):
            if len(visited) == n-1:
                return True
            for y in range(n): 
                if mat[node][y] and y not in visited:
                    visited.add(y)
                    dfs(y, visited)
            if len(visited) == n-1:
                return True
            return False
        for i in range(n):
            seen = set()
            if dfs(i, seen):
                return i
        return -1